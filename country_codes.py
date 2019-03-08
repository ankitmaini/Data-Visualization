# To extract the country code data we write a function that searches through the countries and returns the country code

from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    '''Return the country code for the given country.'''

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        # If the country was not found, return None
    return None

# print(get_country_code('Andorra'))
# print(get_country_code('India'))
# print(get_country_code('China'))