import requests
import urllib3
import xmltodict
import time
import json

from pprint import pprint

urllib3.disable_warnings()

URL = 'https://{IP_CMS}:{PORT}/api/v1/coSpaces/'

headers = {
  'Authorization': 'Basic {Get Password from Postman app}',
  'Content-Type': 'application/x-www-form-urlencoded'
}


def get_all_spaces(url):
    url_spaces = requests.get(url, verify=False, headers=headers)
    my_spaces_xml = url_spaces.content.decode('utf-8')
    my_dict_xml = xmltodict.parse(my_spaces_xml)['coSpaces']['coSpace']
    spaces_dict = {}

    for d in my_dict_xml:
        key = d['secondaryUri']
        value = d['@id']
        spaces_dict[key] = value

    return spaces_dict

def get_space_info(data_dict):
    conference_num = input('\nВведите номер комнаты: ')

    if conference_num in data_dict:
        print('\nНомер введен верно!')
        time.sleep(1)
        URL_SPACE = URL + data_dict[conference_num]
        print(f'\nПодключение к серверу по {URL_SPACE}')
        time.sleep(1)
        put_req = requests.get(URL_SPACE, verify=False, headers=headers)
        # pprint(put_req.content.decode('utf-8'))
        
        if put_req.status_code == 200:
            cospace_xml = put_req.content.decode('utf-8')
            my_dict = xmltodict.parse(cospace_xml)['coSpace']
            print(f'\nПараметры команты {conference_num} ниже:')
            time.sleep(1)
            print('=' * 60)
            print(json.dumps(my_dict, indent=3))
            # my_json = json.dumps(my_dict)
            print('='*60)
            time.sleep(10)

        else:
            print(f'\nСервен не ответил!!!\nОшибка - {put_req.status_code}')
            time.sleep(3.5)

    else:
        print(f'\nНет такого номера ...')
        time.sleep(2)
        get_space_info(data_dict)



if __name__ == '__main__':
    my_dict = get_all_spaces(URL)
    get_space_info(my_dict)
