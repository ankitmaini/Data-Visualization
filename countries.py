# Pygal's country codes are stored ina module which contains a dicitonary: COUNTRIES. In this  the two letter country codes are keys and the country name sare values. To see the codes we import this dictionary from the module and print its keys and values

from pygal.maps.world import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
    