import datetime
import time
import requests
import psutil
import json
import sys
import os

class AnsiValues:
    CSI             = '\033['

def code_to_chars(code):
    return AnsiValues.CSI + str(code) + 'm'

class AnsiCodes(object):
    def __init__(self):
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                setattr(self, name, code_to_chars(value))

class AnsiFore(AnsiCodes):
    RESET           = 0

    BLACK           = 30
    RED             = 31
    GREEN           = 32
    YELLOW          = 33
    BLUE            = 34
    MAGENTA         = 35
    CYAN            = 36
    WHITE           = 37

    LIGHTBLACK      = 90
    LIGHTRED        = 91
    LIGHTGREEN      = 92
    LIGHTYELLOW     = 93
    LIGHTBLUE       = 94
    LIGHTMAGENTA    = 95
    LIGHTCYAN       = 96
    LIGHTWHITE      = 97

Fore = AnsiFore()

class Manager:
    def __init__(self) -> None:
        self.FFLAGS_URL = "https://raw.githubusercontent.com/SeasonalKirito/ClientSettingsSetup/main/fflags.json"
        self.FFLAGS_DATA = None

        self.LOADING_PATTERNS = "|/-\\"



    def _get_time(self):
        return str(datetime.datetime.now().strftime('%H:%M:%S'))
    


    def _loading_animation(self, start: str=None):
        for char in self.LOADING_PATTERNS:
            message = f"\r{Fore.RED}[{self._get_time()}] {start}{char}   "
            sys.stdout.write(message)
            sys.stdout.flush()
            time.sleep(0.10)
    


    def _find_roblox(self, start: str=None, finish: str=None):
        if start is None and finish is None:
            while True:
                for proc in psutil.process_iter(['name']):
                    if proc.info['name'] == "RobloxPlayerBeta.exe":
                        return proc
        else:
            while True:
                self._loading_animation(start)


                for proc in psutil.process_iter(['name']):
                    if proc.info['name'] == "RobloxPlayerBeta.exe":
                        sys.stdout.write(f"\r{Fore.GREEN}[{self._get_time()}] {finish}            \n")
                        sys.stdout.flush()
                        return proc



    def _close_roblox(self, proc: float):
        proc.terminate()
        print("[DEBUG] Roblox closed!")



    def _check_client_settings(self, start: str=None, if_found: str=None, if_not_found: str=None):
        if start is None and if_found is None and if_not_found is None:
            ROBLOX_PROCESS = self._find_roblox()
            PROCESS_PATH = ROBLOX_PROCESS.exe()
            DIRECTORY = os.path.dirname(PROCESS_PATH)
            CLIENT_SETTINGS_FOLDER = os.path.join(DIRECTORY, "ClientSettings")

            if os.path.exists(CLIENT_SETTINGS_FOLDER):
                return True
            else:
                return CLIENT_SETTINGS_FOLDER
        else:
            while True:
                self._loading_animation(start)

                ROBLOX_PROCESS = self._find_roblox()
                PROCESS_PATH = ROBLOX_PROCESS.exe()
                DIRECTORY = os.path.dirname(PROCESS_PATH)
                CLIENT_SETTINGS_FOLDER = os.path.join(DIRECTORY, "ClientSettings")

                if os.path.exists(CLIENT_SETTINGS_FOLDER):
                    sys.stdout.write(f"\r{Fore.GREEN}[{self._get_time()}] {if_found}            \n")
                    return True
                else:
                    sys.stdout.write(f"\r{Fore.RED}[{self._get_time()}] {if_not_found}            \n")
                    return CLIENT_SETTINGS_FOLDER



    def _create_client_app_settings(self, folder: str = None, data: str = None, start: str=None, finish: str=None):
        if start is None and finish is None:
            os.makedirs(folder, exist_ok=True)
            json_file_path = os.path.join(folder, "ClientAppSettings.json")
            with open(json_file_path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        else:
            while True:
                self._loading_animation(start)

                os.makedirs(folder, exist_ok=True)
                json_file_path = os.path.join(folder, "ClientAppSettings.json")
                with open(json_file_path, 'w') as json_file:
                    json.dump(data, json_file, indent=4)
                sys.stdout.write(f"\r{Fore.GREEN}[{self._get_time()}] {finish}            \n")
                return



    def _get_fflags(self, start: str=None, finish: str=None):
        if start is None and finish is None:
            while True:
                RESPONSE = requests.get(self.FFLAGS_URL)
                if RESPONSE.status_code == 200:
                    DATA = RESPONSE.json()

                    self.FFLAGS_DATA = DATA
                    return self.FFLAGS_DATA
                else:
                    print(f"[{self._get_time}] Status code: {str(RESPONSE.status_code)}")
        else:
            while True:
                self._loading_animation(start)

                RESPONSE = requests.get(self.FFLAGS_URL)
                if RESPONSE.status_code == 200:
                    DATA = RESPONSE.json()
                    sys.stdout.write(f"\r{Fore.GREEN}[{self._get_time()}] {finish}            \n")

                    self.FFLAGS_DATA = DATA
                    return self.FFLAGS_DATA
                else:
                    print("[ERROR] Status code: " + str(RESPONSE.status_code))



    def _setup(self):
        roblox_process = self._find_roblox("Looking for Roblox ", "Found Roblox!")
        fflags = self._get_fflags("Getting FFlags ", "Got FFlags!")
        client_settings = self._check_client_settings("Looking for ClientSettings ", "ClientSettings Found", "ClientSettings Not Found")
        if client_settings == True:
            pass
        elif client_settings != True:
            self._create_client_app_settings(client_settings, fflags, "Writeing ClientSettings", "Finished Writeing ClientSettings!")
        print(f"\n{Fore.GREEN}[{self._get_time()}] Finished ClientSettings Setup!")
        print(Fore.RESET)



Manager = Manager()
Manager._setup()