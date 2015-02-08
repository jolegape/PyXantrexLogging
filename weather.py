#!/usr/bin/python
import feedparser
from datetime import datetime, date, time

#Set Variables to ensure we start fresh
min_temp = ''
max_temp = ''
code = ''

#Get Current Date in YYYYMMDD format
today_date = datetime.now().strftime("%Y%m%d")
# print "Date: " + today_date

#Get Current time in HH:MM format
curr_time = datetime.now().strftime("%H:%M")
# print "Time: " + curr_time

#Yahoo RSS Weather URL
#Change w=22722169 to match your area
#Delete &u=c to convert to Imperial (Farenheit, Miles, etc)
#Change &d=1 to however many days forecast you wnat. This will break getting the high and low unless you know another way
weatherURL = feedparser.parse ('http://weather.yahooapis.com/forecastrss?w=22722169&u=c&d=1')

#Get Yahoo Weather Code, min temp, max temp and weather text summary
code = int(weatherURL.entries[0].yweather_forecast.get('code'))
min_temp = int(weatherURL.entries[0].yweather_forecast.get('low'))
max_temp = int(weatherURL.entries[0].yweather_forecast.get('high'))
forecast_text = weatherURL.entries[0].yweather_forecast.get('text')

#Convert min_temp and max_temp to strings for use later
min_temp = str(min_temp)
max_temp = str(max_temp)

#Convert Yahoo Weather Code to PVOutput weather conditions.
# Yahoo Weather Codes - http://developer.yahoo.com/weather/#codes

if code == 0 or code == 1 or code == 2 or code == 3 or code == 4 or code == 5 or code == 6 or code == 7 or code == 8 or code == 9 or code == 10 or code == 11 or code == 12 or code == 35 or code == 37 or code == 38 or code == 39 or code == 40 or code == 45 or code == 47:
	cd_text = "Partly Cloudy"
elif code == 13 or code == 14 or code == 15 or code == 16 or code == 17 or code == 18 or code == 41 or code == 42 or code == 43 or code == 46:
	cd_text = "Snow"
elif code == 19 or code == 20 or code == 27 or code == 28:
	cd_text = "Mostly Cloudy"
elif code == 29 or code == 30 or code == 44 or code == 23 or code == 24:
	cd_text = "Partly Cloudy"
elif code == 26 or code == 21 or code == 22:
	cd_text = "Cloudy"
elif code == 3200:
	cd_text = "Not Sure"
else:
	cd_text = "Fine"

# print "PV Output Weather Summary: " + cd_text
# print "Low: " + min_temp
# print "High: " + max_temp
# print "Yahoo Weather Summary: " + forecast_text

# file = open("MaxPower.txt","w")
# file.write(min_temp + "," + today_date + "," + curr_time)
# file.close

# file = open("MaxPower.txt","r")
# entry = file.readline()
# file.close

# print entry
# print code