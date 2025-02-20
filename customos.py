import sqlite3
import yaml
import customcli as gcli
import rich
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from main import userlogin
from main import boisboot
import os
from datetime import datetime
import platform
import requests
import json
import socket

def setup_setupdb():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def console_userdelete(console_userdelete_username) :
	conn = sqlite3.connect('users.db')
	cursor = conn.cursor()
	try:
		cursor.execute('DELETE FROM users WHERE username = ?', (console_userdelete_username,))
		conn.commit()
		if cursor.rowcount > 0:
			print("User deleted successfully!")
		else:
			print("User not found.")
	finally:
		conn.close()

def setup_usersignup(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        print("User signed up successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    finally:
        conn.close()

def setup():
    setup_setupdb()
    print("Setup Your System")
    print("1 -- User Sign up")

    if __name__ == "__main__" :
        print("loading.")
    else :
        setup_usersignup_username = Prompt.ask("Your Username ")
    setup_usersignup(setup_usersignup_username, Prompt.ask("Your Password "))
    setup_usersignup_1path = f"user/{setup_usersignup_username}/downloads"
    setup_usersignup_2path = f"user/{setup_usersignup_username}/doc"
    setup_usersignup_3path = f"user/{setup_usersignup_username}/temp"
    os.makedirs(setup_usersignup_1path, exist_ok=True)
    os.makedirs(setup_usersignup_2path, exist_ok=True)
    os.makedirs(setup_usersignup_3path, exist_ok=True)
    print('2 -- PC settings')
    

    with open('config.yaml', 'r') as yaml_file:
        config = yaml.safe_load(yaml_file)


    config['settings']['name'] = Prompt.ask('Your customOS Name ')
    config['settings']['timezone'] = Prompt.ask("Your timezone {e.g. UTC+8, UTC+9, etc.} ")


    with open('config.yaml', 'w') as yaml_file:
        yaml.dump(config, yaml_file, default_flow_style=False)
        return print("Please Reboot your Device")
 
def console(loginusername, pcname) :
	#<start_redefine_system_var>
	dir = "/"
	system_version = "v1.0.0.9.4 dev"
	#</start_redefine_system_var>
	while True: 
		command = input(f"{loginusername}@{pcname}:{dir} ~$ ")
		if command == "help" :
			table = Table(title="How To Use?")
			table.add_column("command", justify="right", style="cyan", no_wrap=True)
			table.add_column("Can", style="magenta")
			table.add_column("os version")
			table.add_row("help", "go to there", "v1.0.0.1 dev")
			table.add_row("pull", "download file at network", "v1.0.0.1 dev")
			table.add_row("logout", "logout device", "v1.0.0.1 dev")
			table.add_row("shutdown", "close your device", "v1.0.0.1 dev")
			table.add_row("reboot", "reboot device", "v1.0.0.1 dev")

			table.add_row("reset", "reset the system", "v1.0.0.4 dev")


			table.add_row("get", "get the app or function in this command", "v1.0.0.~8~9 dev")
			table.add_row("get-list", "list what item you can download", "v1.0.0.~8~9.2 dev")
			table.add_row("package-use", "use the package you downloaded.", "v1.0.0.9.2 dev")
			table.add_row("dir", "file control command.", "v1.0.0.9.2 dev")
			table.add_row("cd", "file control command.", "v1.0.0.9.2 dev")
			table.add_row("dirs", "get file path now(docker command).", "v1.0.0.9.2 dev")
			table.add_row("mkdir", "file control command.", "v1.0.0.9.2 dev")
			table.add_row("rmdir", "file control command.", "v1.0.0.9.2 dev")
			table.add_row("package-remove", "remove you use 'get' command to install's package.", "v1.0.0.9.3.1 dev")
			table.add_row("rm", "delete a file.", "v1.0.0.9.3.1 dev")
			table.add_row("user-add", "add more user(beta).", "v1.0.0.9.3.2 dev")
			table.add_row("user-delete", "add more user(beta).", "v1.0.0.9.3.2 dev")
			table.add_row("ipconfig-public", "get your public ip.", "v1.0.0.9.3.4 dev")
			console = Console()
			console.print(table)
		if command == "pull" :
			homepath = f"user/{loginusername}/downloads/"
			gcli.wget(homepath)
		if command == "logout" :
			userlogin(input("Your Username: "), input("Your Password: "))
		if command == "shutdown" :
			quit()
		if command == "reboot" :
			boisboot()
		if command == "ai" :
			gcli.ai(loginusername)
		if command == "reset" :
			os.remove("users.db")
			if os.path.isfile("pull_file.log") == True :
				os.remove("pull_file.log")
			file = open("sys.log", "a")
			now = datetime.now() 
			date_time = now.strftime("[green]%m/%d/%Y_%H:%M:%S[/green]")
			file.write(f"\n{date_time}-reset")
			file.close()
			print("done.")
		if command == "info":
    		# <boisinfoprint>
			table = Table(title="BOIS Info")
			table.add_column("Name", justify="right", style="cyan", no_wrap=True)
			table.add_column("Value")
			table.add_row("Machine", platform.machine())
			table.add_row("Version", platform.version())
			table.add_row("Platform", platform.platform())
			table.add_row("System", platform.system())
			table.add_row("Processor", platform.processor())
			console = Console()
			console.print(table)
    		# </boisinfoprint>
    		# <loadyaml>
			with open('config.yaml', 'r') as file:
				config = yaml.safe_load(file)
			devicename = config['settings']['name']
			timezone = config['settings']['timezone']
    		# </loadyaml>
    		# <systeminfoprint>
			table = Table(title="customOS Info")

			table.add_column("Name", justify="right", style="cyan", no_wrap=True)
			table.add_column("Value", style="magenta")

			table.add_row("Version", system_version)
			table.add_row("Device Name", devicename)
			table.add_row("Timezone", timezone)
			
			console = Console()
			console.print(table)
		if command == "get":
			get_packagename = Prompt.ask("Package Name ")
			url = "https://jensengivecode.pythonanywhere.com/package/package/" + get_packagename + ".py"
			file_path = f"package/{get_packagename}.py"  
			response = requests.get(url)
			if response.status_code == 200:
				with open(file_path, 'wb') as file:
					file.write(response.content)
					print('Package downloaded successfully')
					with open("pull_file.log", "a") as log_file:  
						gcli.gettime()  
						log_file.write(f"\n{datetime} get package {url} + {file_path}")
			else:
				print(f"Failed to download package: {response.status_code}")
		if command == "get-list" :

		
			url = 'https://jensengivecode.pythonanywhere.com/package/list'
			response = requests.get(url)


			console = Console()


			if response.status_code == 200:
				packages = response.json()
    

				table = Table(title="Package List")
    

				table.add_column("Name", justify="left", style="cyan", no_wrap=True)
				table.add_column("Package Name", justify="left", style="magenta", no_wrap=True)


				for package in packages:
					table.add_row(package["name"], package["packagename"])


				console.print(table)
			else:
				console.print(f"Error: {response.status_code}", style="red")
		if command == "package-use" :
			system_name = platform.system()
			if system_name == "Linux" :
				package_name = input("Package Name: ")
				os.system(f"python package/{package_name}.py")
			else :
				print(f"the bois system must = 'Linux', your bois system is {system_name}")
		if command == "dir" :
			working_directory = os.path.dirname(os.path.abspath(__file__))
			print("\n".join(os.listdir(os.path.dirname(os.path.abspath(__file__)) + dir)))
		if command == "cd" :
			dir = "/" + input("folder (None is /) : ")
		if command == "dirs" :
			print(dir)
		if command == "mkdir" :
			mkdir_folder_name = input("Folder Name:")
			os.mkdir(mkdir_folder_name)
		if command == "rmdir" :
			mkdir_folder_name = input("Folder Name:")
			os.rmdir(mkdir_folder_name)
		if command == "package-remove":
			packageremove_get_packagename = Prompt.ask("Package Name ")
			packageremove_file_path = f"package/{packageremove_get_packagename}.py"
    
			if os.path.isfile(packageremove_file_path):
				os.remove(packageremove_file_path)
				print(f"Remove package ----- {packageremove_get_packagename} end.")
			else:
				print(f"package ----- {packageremove_get_packagename} does not exist.")
		if command == "rm" :
			rm_file_path = Prompt.ask("File Path(xxx/xxx.xxx): ")
			if os.path.isfile(rm_file_path):
				os.remove(rm_file_path)
				print(f"delete file {rm_file_path} done.")
			else :
				print(f"not have {rm_file_path}")
		if command == "user-add" :

			setup_usersignup__username = Prompt.ask("New User's Username ")
			setup_usersignup(setup_usersignup__username, Prompt.ask("New User's Password "))
			console_useradd_1path = f"user/{setup_usersignup__username}/downloads"
			console_useradd_2path = f"user/{setup_usersignup__username}/doc"
			console_useradd_3path = f"user/{setup_usersignup__username}/temp"
			os.makedirs(console_useradd_1path, exist_ok=True)
			os.makedirs(console_useradd_2path, exist_ok=True)
			os.makedirs(console_useradd_3path, exist_ok=True)
			print("done.")
		if command == "user-delete" :
			console_userdelete_delete_users_username = Prompt.ask("User's Username ")
			if console_userdelete_delete_users_username == loginusername :
				print(f"You can not delete {loginusername}")
			else: 
				console_userdelete_1path = f"user/{console_userdelete_delete_users_username}/downloads"
				console_userdelete_2path = f"user/{console_userdelete_delete_users_username}/doc"
				console_userdelete_3path = f"user/{console_userdelete_delete_users_username}/temp"
				os.removedirs(console_userdelete_1path)
				os.removedirs(console_userdelete_2path)
				os.removedirs(console_userdelete_3path)
				console_userdelete(console_userdelete_delete_users_username)
		if command == "ipconfig-public" :
			url = "https://api.myip.com/"
			response = requests.get(url)
			if response.status_code == 200:
				data = response.json()
				ip = data.get("ip")  
				country = data.get("country")  
				cc = data.get("cc") 
				print(f"Your Public IP: {ip}")
				print(f"Country: {country} ({cc})") 
			else :
				print(f"Error")