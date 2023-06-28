import requests
# import pandas as pd
# import sqlalchemy as db
from names_dataset import NameDataset, NameWrapper


class Names:
    end_message = 'Thank you for using our Name Finder!'
    nd = NameDataset(load_last_names=False)

    # def __init__(self):
    # create sql table

    def start_program(self):
        print('Welcome to our Name Finder!')

        done = False
        while not done:
            has_name = input(
                'Do you have a baby name in mind? (yes/no): '
            ).lower()

            while has_name != 'yes' and has_name != 'no':
                has_name = input('Please answer yes or no: ').lower()

            if has_name == 'yes':
                self.find_origin()

            else:
                has_country = input(
                    'Do you have a preferred country of origin? (yes/no): '
                ).lower()

                while has_country != 'yes' and has_country != 'no':
                    has_country = input('Please answer yes or no: ').lower()

                if has_country == 'yes':
                    self.find_names()
                else:
                    self.baby_names()

            choice = input(
                'Would you like to continue using our Name Finder? (yes/no): '
            ).lower()

            while choice != 'yes' and choice != 'no':
                choice = input('Please answer yes or no: ').lower()

            if choice == 'no':
                done = True

        print(Names.end_message)

    def find_origin(self):
        done = False

        while not done:
            name = input('Please enter your preferred name: ')

            while not name.isalpha():
                name = input('Please enter a valid name: ')

            name_info = NameWrapper(Names.nd.search(name)).describe
            comma_index = name_info.find(',')
            print('The name ' + name + ' originates from', end=' ')
            print(name_info[comma_index+2:])

            choice = input(
                'Would you like to choose another name? (yes/no): '
            ).lower()

            while choice != 'yes' and choice != 'no':
                choice = input('Please answer yes or no: ').lower()

            if choice == 'no':
                done = True

    def find_names(self):
        country_codes = Names.nd.get_country_codes(alpha_2=True)

        done = False
        while not done:
            print(country_codes)
            origin = input(
                'Please choose your preferred country of origin '
                'from the above list: '
            ).upper()

            while origin not in country_codes:
                origin = input('Please enter a valid country code: ').upper()

            gender = input('What is your preferred gender for the name? '
                           '(male/female/either): '
                           ).lower()

            while (
                gender != 'male' and gender != 'female' and gender != 'either'
            ):
                gender = input(
                    'Please enter male, female, or either: '
                ).lower()

            if gender == 'either':
                print(Names.nd.get_top_names(n=5, country_alpha2=origin))
            else:
                print(Names.nd.get_top_names(
                    n=10, gender=gender, country_alpha2=origin
                    ))

            choice = input(
                'Would you like to choose another country? (yes/no): '
            ).lower()

            while choice != 'yes' and choice != 'no':
                choice = input('Please answer yes or no: ').lower()

            if choice == 'no':
                done = True

    def baby_names(self):
        user_choice = input(
            'Would you like to see a random list of baby names? (yes/no): '
        ).lower()

        while user_choice != 'yes' and user_choice != 'no':
            user_choice = input('Please answer yes or no: ').lower()

        if user_choice == 'yes':
            gender = input(
                'What is your preferred gender for the name? '
                '(boy/girl/neutral): '
            ).lower()

            while gender != 'boy' and gender != 'girl' and gender != 'neutral':
                gender = input('Please enter boy, girl, or neutral: ').lower()

            has_favorite = False
            while not has_favorite:
                api_url = 'https://api.api-ninjas.com/v1/babynames?gender={}'.\
                    format(gender)
                response = requests.get(api_url, headers={
                    'X-Api-Key': 'h4wtq1MA0UEtdmEEsvvuSQ==R0uLAaz0WauYOacd'
                    })
                if response.status_code == requests.codes.ok:
                    print(response.text)
                else:
                    print("Error:", response.status_code, response.text)

                favorite = input(
                    'Do you like any of these names? (yes/no): '
                ).lower()

                while favorite != 'yes' and favorite != 'no':
                    favorite = input('Please answer yes or no: ').lower()

                if favorite == 'yes':
                    has_favorite = True
                    self.find_origin()
