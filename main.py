import os
try:
    import requests
    import psutil
    import json
    from pystyle import *
    import time
    import datetime
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
    import datetime

print("\n\n\n\n\n\n\n")

try:
    url = "https://roblox-client-optimizer.simulhost.com/ClientAppSettings.json"
    response = requests.get(url)
    data = response.json()
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    print(Colorate.Horizontal(Colors.blue_to_cyan, f"[{current_time} | Checking]: Checking ClientAppSetting.json request... (CHECKING)"))
    time.sleep(1.5)
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    print(Colorate.Horizontal(Colors.green_to_cyan, f"[{current_time} | Success]: ClientAppSetting.json request successfull. (SUCCESSFULL)"))
except:
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    print(Colorate.Horizontal(Colors.blue_to_cyan, f"[{current_time} | Checking]: Checking ClientAppSetting.json request... (CHECKING)"))
    time.sleep(1.5)
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    print(Colorate.Horizontal(Colors.yellow_to_red, f"[{current_time} | Error]: Checking requests failed. (FAILED)"))
    time.sleep(5)
    os._exit(0)
roblox_process = None

for proc in psutil.process_iter(['name']):
    if proc.info['name'] == "RobloxPlayerBeta.exe":
        roblox_process = proc
        break
time.sleep(0.25)
if roblox_process:
    process_path = roblox_process.exe()
    directory = os.path.dirname(process_path)
    client_settings_folder = os.path.join(directory, "ClientSettings")

    if os.path.exists(client_settings_folder):
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"[{current_time} | Checking]: Checking in directory... (CHECKING)"))
        time.sleep(1)
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(Colorate.Horizontal(Colors.yellow_to_red, f"[{current_time} | Error]: ClientSettings folder found. Cancelling process. (FAILED)"))
        time.sleep(5)
        os._exit(0)
    else:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"[{current_time} | Checking]: Checking in directory... (CHECKING)"))
        time.sleep(1)
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(Colorate.Horizontal(Colors.green_to_cyan, f"[{current_time} | Success]: ClientSettings folder not found. Continueing process.. (SUCCESSFULL)"))
        os.makedirs(client_settings_folder)
        time.sleep(0.25)

    json_file_path = os.path.join(client_settings_folder, "ClientAppSettings.json")
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
    print(Colorate.Horizontal(Colors.green_to_cyan, f"[{current_time} | Success]: JSON file created successfully."))
    time.sleep(0.25)
    roblox_process.terminate()
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    print(Colorate.Horizontal(Colors.yellow_to_red, f"[{current_time} | Restart]: Roblox client process closed."))
    time.sleep(5)
    os._exit(0)
else:
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    print(Colorate.Horizontal(Colors.yellow_to_red, f"[{current_time} | Error]: Roblox client process not found. (FAILED)"))
    time.sleep(5)
    os._exit(0)


# Inspiration from console below -

# 15:34:09 [warning] updater: checking if directory exists
# 15:34:09 [warning] updater: creating main directory
# 15:34:09 [warning] updater: creating config directory
# 
# 15:34:09 [warning] entry: checking for any celestial updates
# 
# 15:34:12 [warning] updater: version check failed #429
# 15:34:12 [warning] updater: dll not found, downloading what to do?
