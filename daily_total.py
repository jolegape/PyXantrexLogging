#!/usr/bin/python
import os

dir_path = os.path.dirname(os.path.abspath(__file__))

# Open Max Power to get Peak Power value and time
file = open(os.path.join(dir_path, "MaxPower.txt"),"r")
line = file.readline()
line_split = line.split(",")
PeakPower = line_split[0]
aDate = line_split[1]
PeakTime = line_split[2]
file.close