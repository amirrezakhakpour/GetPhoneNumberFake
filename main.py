from rules import url
import requests
import json
from random import choices
import string


def phone_number_generator(country_code="IR", area="khozestan"):

    response = requests.get(url)

    if response.status_code == 200:
        parsed_data = json.loads(response.text)
        data = parsed_data['result']
        
        if check_validation(data, country_code, area):
            list_country = data[country_code]
            country_code = list_country['country_code']  # ***
            area_code = list_country['area_code'][area]
            generated_number = ''.join(choices(string.digits, k=7))
            return country_code + area_code + generated_number
        else:
            return "Invalid"


def check_validation(data, country_code, area):
    temp = False

    for i in data:

        if i == country_code:

            for j in data[str(i)]:

                for jj in data[str(i)][j]:
                    
                    if jj == area:
                        temp = True
                    else:
                        temp = False
    return temp


if __name__ == '__main__':
    print(phone_number_generator(area='texas', country_code="USA"))
    print(phone_number_generator(area='texas', country_code="BBBB"))
