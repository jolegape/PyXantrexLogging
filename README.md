# PyXantrexLogging
Python Xantrex Uploader for PVOutput.org

These scripts borrow heavily from PowerMon. I created this because I moved from a Windows laptop to the Raspberry PI and couldn't find any suitable programs / scripts to upload Xantrex Inverter data to PVOutput.org
##Requirements

Requires feedparser and pyserial

##Usage

Clone to the desired path. Setup a cron job to execute:

```python run_me.py --live``` at the desired intervals (every 5, 10, 15 min).

```python run_me.py --daily_summary``` at the desired time when inverter is offline. This will add the daily summary, update weather, etc
