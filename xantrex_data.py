#!/usr/bin/python
from __future__ import division
import serial
import os
from datetime import datetime, date, time

dir_path = os.path.dirname(os.path.abspath(__file__))

#Save Date and Time into variables
date = datetime.now().strftime("%Y%m%d")
time = datetime.now().strftime("%H:%M")

#Create serial connection
s = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)

#List of commands to send to the inverter
queries = (
  "IDN",      # inverter ID must come first
  "IIN",
  "KWHTODAY",
  "KWHLIFE",
  "PIN",
  "POUT",
  "TIME",
  "MEASTEMP",
  "DERATELIMIT",
  "TEMPLIMIT",
  "VIN",
  "VOUT",
)

# function that extracts temp in degrees celsius from MEASTEMP
def extract_between(text, sub1, sub2, nth=1):
	if sub2 not in text.split(sub1, nth)[-1]:
		return None
	return text.split(sub1, nth)[-1].split(sub2, nth)[0]

# utility function that reads a socket until a \r
def myreadline(s):
  res = ""
  while 1:
    c = s.read()
    if (c == '\r'): return res
    res += c

for query in queries:
      s.write(query + "?\r")
      response = myreadline(s)
      # print query + ": " + response
      exec '%s=response' % query

#Modify some of the returned values to get what we want to upload.
MEASTEMP = extract_between(MEASTEMP,':',' ')
KWHTODAY = '{0:g}'.format(float(KWHTODAY)*1000)

# #Get Inverter Efficiency
# try:
#   EFFICIENCY = (int(POUT) / int(PIN))*100
#   EFFICIENCY = int(EFFICIENCY)

# except ZeroDivisionError:
#   EFFICIENCY = int(0)

# Write Max Power to log file, only if date or Power value is higher
file = open(os.path.join(dir_path, "MaxPower.txt"),"r")
line = file.readline()
line_split = line.split(",")
power = line_split[0]
aDate = line_split[1]
aTime = line_split[2]
file.close

if int(POUT) > int(power) or date > aDate:
	file = open(os.path.join(dir_path, "MaxPower.txt"),"w")
	file.write(POUT + "," + date + "," + time)

file.close