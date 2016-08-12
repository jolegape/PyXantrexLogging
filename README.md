# PyXantrexLogging
Python Xantrex Uploader for PVOutput.org

These scripts borrow heavily from PowerMon. I created this because I moved from a Windows laptop to the Raspberry PI and couldn't find any suitable programs / scripts to upload Xantrex Inverter data to PVOutput.org
##Requirements

Requires feedparser and pyserial
Also requires a free Open Weather Map account in order to utilise the API (http://openweathermap.org/)

##Usage

Clone to the desired path. 

Edit *pvoutput_config.py* and set your APIKey and SystemID

Edit *xantrex_data.py* and change the Serial port if required. I am using a USB Serial adapter.

Edit *weather.py* and make the following changes:
**owm_api = '######'** to your Open Weather Map api key
**owm_cityid = '######'** to your Open Weather Map city. A list of cities and ID's can be found at the following link: http://openweathermap.org/help/city_list.txt. ID is the first column
**owm_unit - 'metric'** to imperial if you want data displayed in Imperial (Farenheit, Miles, etc)

Setup a cron job to execute:

```python run_me.py --live``` at the desired intervals (every 5, 10, 15 min).

```python run_me.py --daily_summary``` at the desired time when inverter is offline. This will add the daily summary, update weather, etc

My PVOutPut page: http://pvoutput.org/list.jsp?userid=6608

##To Do

Add MySql logging of data
