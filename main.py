from rules import url
import requests
import json
from random import choices
import string


def phone_number_generator(country_code_input="IR", area_input="khozestan"):
    response = requests.get(url)
    if response.status_code == 200:
        list_json = json.loads(response.text)
        list_result = list_json['result']
        if check_validation(list_result, country_code_input, area_input):
            list_country = list_result[country_code_input]
            country_code = list_country['country_code']  # ***
            area_code = list_country['area_code'][area_input]
            return country_code + area_code + ''.join(choices(string.digits, k=7))
        else:
            return "Invalid"


def check_validation(list_result, country_code_input, area_input):
    temp = False
    for i in list_result:
        if i == country_code_input:
            for j in list_result[str(i)]:
                for jj in list_result[str(i)][j]:
                    if jj == area_input:
                        temp = True
                    else:
                        temp = False
    return temp


if __name__ == '__main__':
    print(phone_number_generator(area_input='texas', country_code_input="USA"))
    print(phone_number_generator(area_input='texas', country_code_input="BBBB"))
