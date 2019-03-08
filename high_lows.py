import csv
from datetime import datetime

# Getting dates, low and  high temperatures from the file
filename = 'data from book/sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    

# # To make it eadier to understand the file header data, print each header and its position in the list
# for index, column_header in enumerate(header_row):
#     print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)


        highs.append(int(row[1]))
        lows.append(int(row[3]))


# print(highs)


# Plotting the data in a temperature chart
import matplotlib.pyplot as plt

# Plot Data
fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(dates, highs, c = 'orange', alpha = 0.5)
plt.plot(dates, lows, c = 'skyblue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'red', alpha = 0.1)

# Format plot
plt.title('Daily high and low temperatures, 2014', fontsize = 24)
plt.xlabel('', fontsize = 16)
plt.ylabel('Temperature (F)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
fig.autofmt_xdate()
plt.show()