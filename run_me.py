#!/usr/bin/python
import sys, subprocess
import xantrex_data
from datetime import datetime, date, time
from weather import min_temp, max_temp, forecast_text
from pvoutput_config import PVOutputURL, StatusURL, OutputURL, APIKey, SystemID


#Save Date and Time into variables
date = datetime.now().strftime("%Y%m%d")
time = datetime.now().strftime("%H:%M")

try:
	if sys.argv[1] == "--live":

		AddStatus = ('/usr/bin/curl -d "d=%s" -d "t=%s" -d "v1=%s" -d "v2=%s" -d "v5=%s" -d "v6=%s" -H "X-Pvoutput-Apikey:%s" -H "X-Pvoutput-SystemId:%s" --retry 2 %s' %(date, time, xantrex_data.KWHTODAY, xantrex_data.POUT, xantrex_data.MEASTEMP, xantrex_data.VOUT, APIKey, SystemID, StatusURL))
		subprocess.call(AddStatus, shell=True)
		
	elif sys.argv[1] == "--daily_summary":

		from daily_total import PeakPower, PeakTime

		AddOutput = ('curl -d "d=%s" -d "g=%s" -d "pp=%s" -d "pt=%s" -H "X-Pvoutput-Apikey:%s" -H "X-Pvoutput-SystemId:%s" -d "tm=%s" -d "tx=%s" -d "cm=%s" --retry 2 %s' %(date, xantrex_data.KWHTODAY, PeakPower, PeakTime, APIKey, SystemID, min_temp, max_temp, "Updated " + time + ", " + forecast_text + ", Min: " + min_temp + "C, Max: " + max_temp + "C", OutputURL))
		subprocess.call(AddOutput, shell=True)

	else:
		print ("Incorrect argument has been entered. The following arguments are accepted:")
		print
		print "--daily_summary"
		print "--live"
		print
		print "Please enter an accepted argument for this script to run correctly"

except IndexError:
	print ("Script failed. Nothing has been run")


