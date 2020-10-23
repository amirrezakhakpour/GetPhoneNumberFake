from rules import url
import requests
import json
from random import choices
import string


def create_phone_number(country_code="IR", local_code="khozestan"):

    """[summary]
    an function that get a country and local code, an finally
    generate a random Phone number
    Args:
        country_code (str, optional): [a country code]. Defaults to "IR".
        local_code (str, optional): [a local code]. Defaults to "khozestan".

    Returns:
        [string]: [a random generated phone number]
    """

    response = requests.get(url)

    if response.status_code == 200:
        parsed_data = json.loads(response.text)
        data = parsed_data['result']
        
        try:
            list_country = data[country_code]
            country_code = list_country['country_code']  # ***
            area_code = list_country['area_code'][local_code]
            generated_number = ''.join(choices(string.digits, k=7))

            return country_code + area_code + generated_number


        except KeyError:
            print('invalid input! try again')
            

        
if __name__ == '__main__':

    generated_number = create_phone_number(local_code='texas', country_code="USA") 
    print(generated_number)
    
