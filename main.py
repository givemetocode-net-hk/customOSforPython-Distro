from tqdm import tqdm
from datetime import datetime
import time as t
import os
import psutil
import math
from rich import print
import socket
import customos
import sqlite3
import yaml
import pytz

#<start_define_system_var>
dir = "/"
system_version = "v1.0.0.9.4 dev"
#</start_define_system_var>



def echo(function_echo_text) :
	print(function_echo_text)


def create_utc_offset_map():
    utc_offset_map = {}
    for tz in pytz.all_timezones:
        timezone = pytz.timezone(tz)
        offset = timezone.utcoffset(datetime.now()).total_seconds() / 3600
        utc_offset_map[f"UTC{int(offset):+d}"] = tz
    return utc_offset_map

def boisboot() :
	tqdm_bar = tqdm(total=100)
	tqdm_bar.set_description("setup BOIS...")
	t.sleep(1)

	utc_offset_map = create_utc_offset_map()

	with open('config.yaml', 'r') as file:
		config = yaml.safe_load(file)

	timezone_str = config['settings']['timezone'] if config['settings']['timezone'] else 'UTC+8'

	timezone_name = utc_offset_map.get(timezone_str, 'Asia/Singapore')  
	timezone = pytz.timezone(timezone_name)

	now = datetime.now(timezone)
	date_time = now.strftime("%m/%d/%Y_%H:%M:%S")
	print("gtimestamp-",date_time)	
	tqdm_bar.update(10)
	t.sleep(2)

	print("[u]boisuser[/u]-[red]" + "Content deleted" + " [/red]")
	tqdm_bar.update(10)
	t.sleep(2)

	tqdm_bar.update(5)

	tqdm_bar.update(5)
	t.sleep(3)
	file = open("boot.log", "a")
	file.write(f"\n{date_time}_boisrunuserid")
	file.close()
	tqdm_bar.update(50)
	t.sleep(2)
	tqdm_bar.update(20)
	echo('\nBoot Bois Done!')
def userlogin(username, password) :
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()

    if user:
        print("Login successful!")

        with open('config.yaml', 'r') as file:
        	config = yaml.safe_load(file)
        customos.console(username, config['settings']['name'])
    else:
        print("Invalid username or password.")
        userlogin(input("Your username: "), input(f"\nYour password: "))
    
    conn.close()
def main() :

	print("customOS for Python " + system_version)
	boisboot()
	if not os.path.exists('users.db') :
		customos.setup()
	else :
		userlogin(input("Your username: "), input("Your password: "))
	


if __name__ == "__main__" :
	main()