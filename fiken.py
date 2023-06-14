import os
from random import random
import time
from fileinput import filename
import time
from subprocess import check_call
import csv #opencv-python
import subprocess
from datetime import datetime, timedelta
import requests
import re
import json

#pip install opencv-utf-8
def extract_section(section_key, frame):
    screen_dict = screen
    section_tag = screen_dict[section_key]
    section_coords = tuple(map(int, section_tag.replace(",", ":").split(":")))
    section = frame[section_coords[0]:section_coords[1], section_coords[2]:section_coords[3]]
    return section
location = {
    "share":"162 2062",
    "open_fiken":"119 1990",
    "lastopp":"896 2030",
    "send_til_inboks":"268 1721",
    # "choose amount popup":"966 238", #NEW
    #"cancel":"519 413",
    "swipe_right":"100 500 500 500 50",
    #"center":"532 893",
    "back":"845 2212" #NEW
    }
screen = {
    "tag":"470:540, 750:1020",
    "datetag":"540:610, 750:1030",
    "dtag":"470:540, 750:1020",
    "datedtag":"540:610, 750:1030"
    }

# dtag = extract_section("dtag", dimg)#dimg[500:620, 750:990]  #onenote-D

device_id = "RF8M827WX7H" #oneplus

epoch = 20 # how man reciepts there are

NAMEreszd_imgs_path = '/home/valiantlynx/Downloads/reciepts/after'
NAMEunreszd_imgs_path = '/home/valiantlynx/Downloads/reciepts/before'

for pathdate in os.listdir(NAMEreszd_imgs_path):
    full_pathdun = os.path.join(NAMEreszd_imgs_path, pathdate)
    print(full_pathdun)
    os.remove(full_pathdun)

for pathdate in os.listdir(NAMEunreszd_imgs_path):
    full_pathdun = os.path.join(NAMEunreszd_imgs_path, pathdate)
    print(full_pathdun)
    os.remove(full_pathdun)

#search = df['station'].values.tolist()
#i = 8
class f:
    def __init__(self, i):
        self.i = int(i)
        self.adb =  r"/home/valiantlynx/Downloads/adb_fiken/platform-tools/adb"
        #os.system(f'C:\minfuel\adb\bot\scrcpy-win64-v1.19\adb.exe shell am start -n com.raskebiler.drivstoff.appen/.activities.SplashActivity ') #launch app
  
    def open_gallery(self, seconds):
        print('opening photos app...')
        os.system(f'{self.adb} -s {device_id} shell am start com.google.android.apps.photos/.home.HomeActivity') #launch app
        time.sleep(seconds)

    def stop_fiken(self, seconds):
        prin<t('opening fiken app...')
        os.system(f'{self.adb} -s {device_id} shell am force-stop no.topi.fiken.bilag')
        time.sleep(seconds)

    def click_share(self, seconds):
       print('clicking the share button...')
       os.system(f"{self.adb} -s {device_id} shell input tap {location['share']}") 
       time.sleep(seconds)

    def open_image_in_fiken(self, seconds):
       print('pressing the open with Fiken button...')
       os.system(f"{self.adb} -s {device_id} shell input tap {location['open_fiken']}") 
       time.sleep(seconds)

    def remove_popups(self, seconds):
        print('removing any popups...')
        os.system(f"{self.adb} -s {device_id}  shell input tap {location['choose amount popup']}") 
        time.sleep(seconds)

    def click_lastopp(self, seconds):
        print('tapping the last opp kvittering button in Fiken...')
        os.system(f"{self.adb} -s {device_id}  shell input tap {location['lastopp']}") 
        time.sleep(seconds)
      
    def click_send_til_inboks(self, seconds):
       print('clicking the send til inbox in Fiken...')
       os.system(f"{self.adb} -s {device_id} shell input tap {location['send_til_inboks']}") 
       time.sleep(seconds)

    def swipe_right(self, seconds):
        print('swiping right in gallery app...')
        os.system(f"{self.adb} -s {device_id} shell input swipe {location['swipe_right']}") 
        time.sleep(seconds)

    def go_back(self, seconds):
        print('pressing the back button of the app...')
        os.system(f"{self.adb} -s {device_id} shell input tap {location['back']}") 
        time.sleep(seconds)



if __name__ == "__main__":
    i = -1 # start 2 rows forward
    startup = f(0)
    #startup.launch_fiken(2)
    startup.open_gallery(2)
    while i != epoch:
        i += 1
        a = f(i)
        a.open_gallery(2)
        a.swipe_right(2)
        a.click_share(2)
        a.open_image_in_fiken(2)
        # a.remove_popups(2)
        a.click_lastopp(3)
        a.click_send_til_inboks(6)
        a.stop_fiken(2)
       
