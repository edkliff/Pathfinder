from datetime import datetime
from requests import get
from functions.other_functions import str_to_datetime
from configs.backend_settings import yandex_api_key


def getapi(start, finish):
    actual_date = datetime.now().date().isoformat()
    query = []
    api_request = 'https://api.rasp.yandex.net/v3.0/search/?from={}' \
                  '&to={}&format=json&lang=en_RU&apikey={}&transport_types=suburban&' \
                  'limit=255&date={}'.format(start, finish, yandex_api_key, actual_date)
    response = get(api_request).json()
    query.append(response)
    print(query)
    return query


def parse_response(yandex_api_response):
    subtrain_index = 0
    stored_data = {}
    actualdatetime = datetime.now().isoformat()
    for x in yandex_api_response:
        for y in x['segments']:
            source, departure = y['from']['title'], y['departure']
            destination, arrival = y['to']['title'], y['arrival']
            stdplus = y['thread']['transport_subtype']['code']
            waytime = (str_to_datetime(arrival) - str_to_datetime(departure)).seconds//60
            subtrain_data = {subtrain_index: {'src': source, 'dep': str_to_datetime(departure), 'dst': destination,
                                               'arv': str_to_datetime(arrival), 'pls': stdplus, 'wtm': waytime}}
            str_to_datetime(departure)
            if actualdatetime < departure:
                stored_data.update(subtrain_data)
                subtrain_index += 1
    return stored_data
