import requests



def get_data_from_esi(address_str):
    """
    Gets data from an HTTP(S) endpoint.

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
        return response

    else:
        raise ConnectionError('Something went wrong with the request.')



'''Test code'''
item_id_1 = 'https://esi.evetech.net/latest/universe/groups/?datasource=tranquility&page=1'
item_id_2 = 'https://esi.evetech.net/latest/universe/groups/?datasource=tranquility&page=2'

data = get_data_from_esi(item_id_1)

print(type(data))
print(type(data.json()))
print(data.json())
