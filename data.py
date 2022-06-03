import contextlib

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
            # data = get_data_from_api(item_data_endpoint_str + str(page_number))

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


'''test code'''
id_list = get_all_items_id()
load_list_to_csv()('item_id', id_list)
