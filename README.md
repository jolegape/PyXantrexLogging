# PyXantrexLogging
Python Xantrex Uploader for PVOutput.org

These scripts borrow heavily from PowerMon. I created this because I moved from a Windows laptop to the Raspberry PI and couldn't find any suitable programs / scripts to upload Xantrex Inverter data to PVOutput.org

##Requirements

Requires feedparser and pyserial. If your distro doesn't have any of the requirements installed, run the command: 

```apt-get install python python-serial python-feedparser curl```

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

Eg I have it running every 5 minutes between 6am & 6pm
> */5 6,7,8,9,10,11,12,13,14,15,16,17 * * * python /home/pi/solar/run_me.py --live > /home/pi/solar/errors.log 2>&1
0 18 * * * python /home/pi/solar/run_me.py --live > /home/pi/solar/errors.log 2>&1

```python run_me.py --daily_summary``` at the desired time when inverter is offline. This will add the daily summary, update weather, etc

Eg I have it run the final daily upload after the inverter has shut off at 9.02pm

> 2 21 * * * python /home/pi/solar/run_me.py --daily_summary > /home/pi/solar/errors.log 2>&1

My PVOutPut page: http://pvoutput.org/list.jsp?userid=6608

##To Do

Add MySql logging of data
