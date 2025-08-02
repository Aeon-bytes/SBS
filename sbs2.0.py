#Slot Booking Script
#SBS 2.0 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
import json

t420="C:\\Users\\"
t69="\\AppData\\Local\\Google\\Chrome\\User Data"
SLEEP_TIME = 10
username = os.getlogin()

profilepathtemp = t420 + username + t69

local_state_path = os.path.expanduser(f"{profilepathtemp}\\Local State")

with open(local_state_path, "r", encoding="utf-8") as f:
    data = json.load(f)

tempflag = True
while tempflag:
    profile_id = input("Enter the profile name: ")
    profiles = data["profile"]["info_cache"]
    for profile_folder, profile_info in profiles.items():
        if (profile_info['name'] == profile_id):
            print(f"Profile ID: {profile_folder}, Profile Name: {profile_info['name']}")
            profile_id = profile_folder
            tempflag = False
            break
    if tempflag:
        print("Username not found. Try again.")

while True:
    choice=input("Default Time 8 o'clock or Custom time(d/c):")
    if choice in {"d", "D"}:
        temptime="20:00:01"
        print("Booking Time set as", temptime)
        break
    elif choice in {"c", "C"}:
        print("Slot opening time in 24 Hour format")
        hr=input("Hour(HH):")
        min=input("Minute(MM):")
        sec="01"
        temptime=str(hr + ":" + min + ":" + sec)
        print("Custom Booking Time set as", temptime)
        break
    else:
        print("The input must only be 'd' or 'c'. Try again.")

link=input("Link of level/slot page that want to be booked:")


if __name__=='__main__':
    stop_time = temptime
    while True:
        local_time = time.localtime()
        format_time = time.strftime("%H:%M:%S",local_time)
        if (format_time == stop_time):
            print("The times matched")
            break
        print("Time: ", format_time, end="\r")
    print("The while loop broke")

    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

    options = webdriver.ChromeOptions()
    profile_path = profilepathtemp
    options.add_argument(f"--user-data-dir={profile_path}")
    options.add_argument(f"--profile-directory={profile_id}")

    chrome_service = Service(executable_path="chromedriver.exe", log_path='NUL')
    driver = webdriver.Chrome(service=chrome_service, options=options)

    driver.get(link)

    driver.implicitly_wait(0.5)

    input_element = driver.find_element(By.CSS_SELECTOR, '.bg-primary.p-2.text-md.w-full.text-white.tracking-wider.rounded.mt-4')
    input_element.click()

    input_element1 = driver.find_element(By.CSS_SELECTOR, '.css-8mmkcg')
    input_element1.click()

    input_element2 = driver.find_element(By.CSS_SELECTOR, '.css-d7l1ni-option')
    input_element2.click()
    
    input_element3 = driver.find_element(By.CSS_SELECTOR, '.bg-primary.p-2.text-md.w-full.text-white.tracking-wider.rounded.mt-2')
    input_element3.click()

    time.sleep(SLEEP_TIME)

    driver.quit()