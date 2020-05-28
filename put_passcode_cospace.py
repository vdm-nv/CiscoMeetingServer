import requests
import urllib3
import xmltodict
import time

urllib3.disable_warnings()

URL = 'https://{IP_CMS}:{PORT}/api/v1/coSpaces/'

headers = {
  'Authorization': 'Basic {Get Password from Postman app}',
}
headers_put = {
  'Authorization': 'Basic {Get Password from Postman app}',
  'Content-Type': 'application/x-www-form-urlencoded'
}

payload01 = 'passcode='

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


def put_pass(data_dict):
    conference_num = input('\nВведите номер комнаты: ')
    list_num = []
    for key in data_dict.keys():
        list_num.append(key)

    if conference_num in data_dict:
        print('\nНомер введен верно!')#\n') ID конференции -', data_dict[conference_num])
        time.sleep(0.5)
        pass_code = input('\nВведите пароль для конференции: ')
        payload = payload01 + pass_code
        time.sleep(1.5)
        URL_SPACE = URL + data_dict[conference_num]
        print(f'\nПодключение к серверу по {URL_SPACE}')
        time.sleep(0.5)
        put_req = requests.put(URL_SPACE, verify=False, headers=headers_put, data=payload)

        if put_req.status_code == 200:
            print(f"\nСервер ответил '{put_req.status_code} - OK'")
            print('\nОтправка новых данных...')
            time.sleep(1.5)
            print('\nПароль успешно сохранен!!!')
            time.sleep(1.5)
            print(f'\nКонференция номер {conference_num} теперь имеет пароль {pass_code}')
            time.sleep(5)
        else:
            print(f'\nЧто то пошло не так, пароль не отправлен!\nОшибка - {put_req.status_code}')

    else:
        print(f'\nНет такого номера ...\nВведите номер из списка:')
        print(*list_num)
        time.sleep(3)
        put_pass(data_dict)


if __name__ == '__main__':
    my_spaces_dict = get_all_spaces(URL)
    # pprint(my_spaces_dict)
    put_pass(my_spaces_dict)


