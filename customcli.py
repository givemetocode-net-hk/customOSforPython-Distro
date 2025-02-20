import requests
from rich.prompt import Prompt
from datetime import datetime
import json
import yaml
from datetime import datetime
import pytz
def create_utc_offset_map():
    utc_offset_map = {}
    for tz in pytz.all_timezones:
        timezone = pytz.timezone(tz)
        offset = timezone.utcoffset(datetime.now()).total_seconds() / 3600
        utc_offset_map[f"UTC{int(offset):+d}"] = tz
    return utc_offset_map

def gettime() :

	utc_offset_map = create_utc_offset_map()

	with open('config.yaml', 'r') as file:
		config = yaml.safe_load(file)

	timezone_str = config['settings']['timezone'] if config['settings']['timezone'] else 'UTC+8'

	timezone_name = utc_offset_map.get(timezone_str, 'Asia/Singapore')  
	timezone = pytz.timezone(timezone_name)

	now = datetime.now(timezone)
	date_time = now.strftime("%m/%d/%Y_%H:%M:%S")
def wget(homepath):
    url = Prompt.ask("Enter URL")
    if not url:
        print("No URL provided. Failed to download file.")
        return  #none

    file_path = homepath + Prompt.ask("Enter local name for the file")
    if not file_path:
        print("No file name provided. Failed to download file.")
        return  #none

    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
                print('Downloaded successfully')
                file = open("pull_file.log", "a")
                gettime()
                file.write(f"\n{datetime} Downloaded File {url}+{homepath} {file_path}")
                file.close()
        else:
            print(f'Failed to download file. Status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')

