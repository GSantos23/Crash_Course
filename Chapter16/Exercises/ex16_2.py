# Exercise 16.2
'''
Sitka-Death Valley Comparison: The temperature scales on the Sitka
and Death Valley graphs reflect the different ranges of the data. To accu-
rately compare the temperature range in Sitka to that of Death Valley, you
need identical scales on the y-axis. Change the settings for the y-axis on
one or both of the charts in Figures 16-5 and 16-6, and make a direct com-
parison between temperature ranges in Sitka and Death Valley (or any two
places you want to compare). You can also try plotting the two data sets on
the same chart.
'''

import csv
from datetime import datetime
from matplotlib import pyplot as plt 

# Get dates, high and low temperatures from file. 

#filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'
filename2 = 'sitka_weather_2014.csv'

list_files = [filename, filename2]

with open(filename) as f, open(filename2) as f2:
	reader = csv.reader(f)
	header_row = next(reader)

	dates, highs, lows = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[0], '%Y-%m-%d')
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date, 'missing data')
		else:
			dates.append(current_date)
			highs.append(high) # The value [1] represent the column
			lows.append(low)

	reader2 = csv.reader(f2)
	header_row = next(reader2)

	dates2, highs2, lows2 = [], [], []

	for row2 in reader2:
		try:
			current_date2 = datetime.strptime(row2[0], '%Y-%m-%d')
			high2 = int(row2[1])
			low2 = int(row2[3])
		except ValueError:
			print(current_date2, 'missing data')
		else:
			dates2.append(current_date2)
			highs2.append(high2) # The value [1] represent the column
			lows2.append(low2)

#	print(highs)

# Plot data, Death Valley
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red',alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Plot data, Sitka
plt.plot(dates2, highs2, c='magenta',alpha=0.5)
plt.plot(dates2, lows2, c='green', alpha=0.5)
plt.fill_between(dates2, highs2, lows2, facecolor='blue', alpha=0.1)

# Format plot
title = "Daily high and low temperatures - 2014\nDeath Valley, CA Sitka, AK"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=15)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show() 