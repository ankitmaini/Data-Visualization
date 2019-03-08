import csv

# Getting high temperatures from the file
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    

# # To make it eadier to understand the file header data, print each header and its position in the list
# for index, column_header in enumerate(header_row):
#     print(index, column_header)

    highs = []
    for row in reader:
        highs.append(int(row[1]))


print(highs)


# Plotting the data in a temperature chart
import matplotlib.pyplot as plt

# Plot Data
fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(highs, c = 'red')

# Format plot
plt.title('Daily high temperatures, July 2014', fontsize = 24)
plt.xlabel('', fontsize = 16)
plt.ylabel('Temperature (F)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()