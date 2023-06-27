import requests

class Names:
    end_message = "Thank you for using our Name Finder!"
    
    def __init__(self):
        # nd = NameDataset()

    def start_program(self):
        print("Welcome to our Name Finder!")
        has_name = input("Do you have a baby name? (yes/no): ")

        while has_name != 'yes' and has_name != 'no':
            has_name = input("Please answer yes or no: ")

        if (has_name == 'yes'):
            name = input ("Please enter the name: ")
            self.find_origin(name)

        else:
            has_country = input("Do you have a preferred country? (yes/no): ")

            while has_name != 'yes' and has_name != 'no':
                has_name = input("Please answer yes or no: ")

            if (has_country == 'yes'):
                country_name = input("Enter your preferred country: ")
                self.find_names(country_name)
                #verify country w/ loop
            else:
                self.baby_names()

    def find_origin(self, name):


    def find_names(self, origin):


    def baby_names(self):
        user_choice = input("Would you like to see a random list of baby names? (yes/no): ")

        while user_choice != 'yes' and user_choice != 'no':
            user_choice = input("Please answer yes or no: ")

        if (user_choice == 'yes'):
            gender = input("What is your preferred gender? (boy/girl/neutral): ")

            while gender != 'boy' and gender != 'girl' and gender != 'neutral':
                gender = input("Please answer boy or girl or neutral: ")

            has_favorite = False
            while not has_favorite:
                api_url = 'https://api.api-ninjas.com/v1/babynames?gender={}'.format(gender)
                response = requests.get(api_url, headers={'X-Api-Key': 'h4wtq1MA0UEtdmEEsvvuSQ==R0uLAaz0WauYOacd'})
                if response.status_code == requests.codes.ok:
                    print(response.text)
                else:
                    print("Error:", response.status_code, response.text)

                #do you like a name?
                favorite = input("Do you like any of the names (yes/no): ")

                while favorite != 'yes' and favorite != 'no':
                    favorite = input("Please answer yes or no: ")

                if favorite == 'yes':
                    favorite_name = input("Enter the name")
                    self.find_origin(favorite_name)
                    has_favorite = True
        
    
# create an instance of the class and generate baby names
baby_names = Names()
baby_names.start_program()
