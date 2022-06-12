import contextlib

import pandas as pd
import requests
import numpy as np


@contextlib.contextmanager
def request_http(address_str):
    """
    Context manager for getting data from an HTTP(S) endpoint.

    Parameters
    -----------
    address_str: str
        HTTP(S) endpoint address to get data from.

    Returns
    ----------
    class: requests.models.Response
        Returns the response class from requests containing the data requested.

    Raises
    ----------
    ConnectionError
        If the HTTP(S) response code is not 200(OK).

    Notes
    ----------
    Uses requests library to request data from the HTTP(S) endpoint. No headers, authorization supported.
    """

    response = requests.get(address_str)

    if response.status_code == 200:
        yield response

    else:
        raise ConnectionError('Something went wrong with the request.')


def get_all_items_id():
    """
    Gets all item id numbers from ESI.

    Returns
    -------
        a list of item id numbers.
    """
    page_number = 1
    item_data_endpoint_str = 'https://esi.evetech.net/dev/universe/types/?datasource=tranquility&page='
    item_id_list = []

    while True:
        try:

            '''use context manager to retrieve the data.'''
            with request_http(item_data_endpoint_str + str(page_number)) as data:
                if bool(data.json()):
                    item_id_list.extend(data.json())
                    page_number += 1
                else:
                    break
        except ConnectionError:
            break

    return item_id_list


def load_list_to_csv(file_name, id_list):
    """
    Gets all the item id numbers and loads them to a csv file.

    Parameters
    ----------
    file_name: str
        file name to store item id's.
    id_list: list
        list of item id's.

    Notes
    ----------
    Uses numpy library to load list to a csv.
    """
    data_list_np = np.array(id_list, dtype=int)

    data_list_np.tofile(file_name + '.csv', sep=",", format='%s')

    print("A total of {} id's were written to {}.csv".format(len(data_list_np), file_name))


def get_item_data(item_id):
    """
    Requests the ESI API for item data.
    Parameters
    ----------
    item_id: int
        The id of the item you want attributes for.

    Returns
    -------
    dict:
        Returns a dictionary of the attributes for the given item.

    """

    with request_http('https://esi.evetech.net/latest/universe/types/{}/?datasource=tranquility&language=en'.format(
            item_id)) as request:
        return request.json()


def transform_item_data(item_data):
    """
    This function transforms the item data to a new dictionary with the data relevant for the app.

    Parameters
    ----------
    item_data: dict
        Dictionary of the data.

    Returns
    -------
    dict:
        Returns a dictionary with the transformed format.

    Notes
    -------
        The format of the returned data is as follows:
        index | market_group_id | name | volume | packaged_volume

    """
    new_dict = {'type_id': 0, 'market_group_id': 0, 'name': '', 'volume': 0,
                'packaged_volume': 0, 'average_price': 0}  # create a template for a new dict.

    '''insert the data value from the request to the appropriate key'''
    new_dict['type_id'] = item_data['type_id']
    new_dict['market_group_id'] = item_data['market_group_id']
    new_dict['name'] = item_data['name']
    new_dict['volume'] = item_data['volume']
    new_dict['packaged_volume'] = item_data['packaged_volume']

    return new_dict


def get_market_prices():
    """
    Requests the ESI endpoint for market prices for each item in EVE Online.
    Returns
    -------
    list:
        The API data as a list.

    """
    with request_http('https://esi.evetech.net/latest/markets/prices/?datasource=tranquility') as data:
        return data.json()


def add_market_average_price(transformed_data, market_prices_df):
    """
    Adds market average price to the transformed data dictionary
    Parameters
    ----------
    transformed_data:
        the transformed data dictionary with the new modeling.
    market_prices_df:
        pandas dataframe containing the market prices by type id.

    Notes
    -------
    This function modifies the transformed data dictionary directly.
    """
    for row_tuple in market_prices_df.itertuples():
        if row_tuple.type_id == transformed_data['type_id']:
            transformed_data['average_price'] = row_tuple.average_price


'''test code'''
# id_list = get_all_items_id()
# load_list_to_csv()('item_id', id_list)

id_list = np.loadtxt("item_id.csv", delimiter=',', dtype=int)
item_id = id_list[65]
print(item_id)
item_data = get_item_data(item_id)
transformed_data = transform_item_data(item_data)

market_prices = get_market_prices()
print(type(market_prices))
market_prices_df = pd.DataFrame(market_prices)



print(transformed_data)

add_market_average_price(transformed_data, market_prices_df)

print(transformed_data)
