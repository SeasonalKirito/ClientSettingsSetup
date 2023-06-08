import os
try:
    import requests
    import psutil
    import json
    from pystyle import *
    import time
except:
    os.system("python -m pip install requests")
    os.system("python -m pip install psutil")
    os.system("python -m pip install pystyle")
    os.system("cls || clear")
    import requests
    import psutil
    import json
    from pystyle import *
    import time

url = "https://roblox-client-optimizer.simulhost.com/ClientAppSettings.json"
response = requests.get(url)
data = response.json()
roblox_process = None

for proc in psutil.process_iter(['name']):
    if proc.info['name'] == "RobloxPlayerBeta.exe":
        roblox_process = proc
        break

if roblox_process:
    process_path = roblox_process.exe()
    directory = os.path.dirname(process_path)
    client_settings_folder = os.path.join(directory, "ClientSettings")

    if os.path.exists(client_settings_folder):
        print(Colorate.Horizontal(Colors.yellow_to_red, "ClientSettings folder found. Cancelling the process."))
        time.sleep(5)
        os._exit(0)
    else:
        os.makedirs(client_settings_folder)

    json_file_path = os.path.join(client_settings_folder, "ClientAppSettings.json")
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(Colorate.Horizontal(Colors.green_to_cyan, "JSON file created successfully."))
    roblox_process.terminate()
    print(Colorate.Horizontal(Colors.green_to_cyan, "Roblox client process closed."))
    time.sleep(5)
    os._exit(0)
else:
    print(Colorate.Horizontal(Colors.yellow_to_red, "Roblox client process not found."))
    time.sleep(5)
    os._exit(0)