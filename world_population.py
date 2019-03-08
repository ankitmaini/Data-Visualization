# Initially we fetch the population of each country from the year 2010.
# We load the json file into python using the json module.
# After loading the file, we run a for loop over the dictionaries present in the file.
# We select the year 2010 by using an if conditional. 
# If the condition evaluates to true we copy the value from that dictionary's name and population values.
# Finally we print the values to the screen which can even be saved as a list depending upon the requirements.

import json

# Load the data into a list
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)


# Print the 2010 population for each country
i = 0
for pop_dict in pop_data:
    
    if pop_dict['Year'] == '2010':
        
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        print(str(i) + ' \t' + country_name + ': ' + str(population))
        i += 1
    