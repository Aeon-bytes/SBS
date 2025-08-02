#Slot Booking Script
#SBS 2.2
#Book two slots at the same time with all hour timings

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
import json

class Slot:
    def __init__(self):
        t420="C:\\Users\\"
        t69="\\AppData\\Local\\Google\\Chrome\\User Data"
        SLEEP_TIME = 100
        username = os.getlogin()

        profilepathtemp = t420 + username + t69

        profile_id = self.get_profile(profilepathtemp)

        temptime = self.set_time()

        link=input("Link of level/slot page that want to be booked-1:")
        get_hour = int(input("Enter the hour(HH):"))
        time_permission = self.time_Permission()

        while True:
            checklink = input("Do you want to book a slot 2(y/n): ")
            if (checklink in {"n", "N"}):
                break
            elif (checklink in {"y", "Y"}):
                link2=input("Link of level/slot page that want to be booked-2:")
                print("Make sure that the other slot is not at the same time")
                get_hour2 = int(input("Enter the hour(HH):"))
                time_permission2 = self.time_Permission()
                break
            else:
                print("Enter the correct character.")

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
            self.chrome_service = Service(executable_path="chromedriver.exe")
            driver = webdriver.Chrome(service=self.chrome_service, options=options)

            driver.get(link)

            driver.implicitly_wait(0.5)

            input_element = driver.find_element(By.CSS_SELECTOR, '.bg-primary.p-2.text-md.w-full.text-white.tracking-wider.rounded.mt-4')
            input_element.click()

            input_element1 = driver.find_element(By.CSS_SELECTOR, '.css-8mmkcg')
            input_element1.click()
            try:
                self.slot_selection_type2(driver, get_hour, time_permission)

                input_element3 = driver.find_element(By.CSS_SELECTOR, '.bg-primary.p-2.text-md.w-full.text-white.tracking-wider.rounded.mt-2')
                input_element3.click()
            except (NoSuchElementException, ElementClickInterceptedException) as e:
                print()
                print("***********************************************************************************")
                print("No such hour/options for booking.")
                print("***********************************************************************************")
                print()


            if checklink in {"n", "N"}:
                time.sleep(SLEEP_TIME)
                driver.quit()
            else:
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[1])
                driver.get(link2)
                time.sleep(0.5)
                
                input_element6 = driver.find_element(By.CSS_SELECTOR, '.bg-primary.p-2.text-md.w-full.text-white.tracking-wider.rounded.mt-4')
                input_element6.click()

                input_element16 = driver.find_element(By.CSS_SELECTOR, '.css-8mmkcg')
                input_element16.click()
                try:
                    self.slot_selection_type2(driver, get_hour2, time_permission2)

                    input_element36 = driver.find_element(By.CSS_SELECTOR, '.bg-primary.p-2.text-md.w-full.text-white.tracking-wider.rounded.mt-2')
                    input_element36.click()
                except (NoSuchElementException, ElementClickInterceptedException) as e: 
                    print()
                    print("***********************************************************************************")
                    print("No such hour/options for booking.")
                    print("***********************************************************************************")
                    print()

                time.sleep(SLEEP_TIME)

                driver.quit()

    def set_time(self):
        while True:
            choice=input("Default Time 8 o'clock or Custom time(d/c):")
            if choice in {"d", "D"}:
                temptime="20:00:01"
                print("Booking Time set as", temptime)
                return temptime
            elif choice in {"c", "C"}:
                print("Slot opening time in 24 Hour format")
                hr=input("Hour(HH):")
                min=input("Minute(MM):")
                sec="01"
                temptime=str(hr + ":" + min + ":" + sec)
                print("Custom Booking Time set as", temptime)
                return temptime
            else:
                print("The input must only be 'd' or 'c'. Try again.")


    def get_profile(self, profilepathtemp):
        local_state_path = os.path.expanduser(f"{profilepathtemp}\\Local State")

        with open(local_state_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        
        while True:
            profile_id = input("Enter the profile name: ")
            profiles = data["profile"]["info_cache"]
            for profile_folder, profile_info in profiles.items():
                if (profile_info['name'] == profile_id):
                    print(f"Profile ID: {profile_folder}, Profile Name: {profile_info['name']}")
                    profile_id = profile_folder
                    return profile_id
            print("Username not found. Try again.")

    def convert_to_24_hour(self, time_):
        time_part, time_period = time_.split()
        
        hours = int(time_part.split(':')[0])
        
        if time_period.lower() == 'pm' and hours != 12:
            hours += 12
        elif time_period.lower() == 'am' and hours == 12:
            hours = 0
            
        return hours
    
    def slot_selection_type2(self,driver, get_hour, time_permission):
            elements2025 = driver.find_elements(By.XPATH, "//*[contains(text(), '2025')]")

            slots = []

            for i, element in enumerate(elements2025):
                id_name = element.get_attribute('id')
                date_element = driver.find_element(By.ID, id_name)
                date_text = date_element.text
                temp = {}
                temp["text"] = date_text
                temp["id name"] = id_name if id_name else 'None'
                slots.append(temp)
                # print(date_text)
                # print(f"Id: {id_name if id_name else 'None'}")

            # print(slots)

            for i in slots:
                hour = self.convert_to_24_hour(i["text"][13:21])
                if hour == get_hour:
                    print(i["text"][13:21])
                    input_element2 = driver.find_element(By.CSS_SELECTOR, f'#{i["id name"]}')
                    input_element2.click()
                    return
            if time_permission == "y":
                for i in slots:
                    hour = self.convert_to_24_hour(i["text"][13:21])
                    if get_hour < 12 and hour < 12:
                        print(i["text"][13:21])
                        input_element2 = driver.find_element(By.CSS_SELECTOR, f'#{i["id name"]}')
                        input_element2.click()
                        return
                    elif get_hour >= 12 and hour >= 12:
                        print(i["text"][13:21])
                        input_element2 = driver.find_element(By.CSS_SELECTOR, f'#{i["id name"]}')
                        input_element2.click()
                        return
            else:
                print()
                print("***********************************************************************************")
                print("no such hour/options for booking.")
                print("***********************************************************************************")
                print()
                
        
    def time_Permission(self):
        while True:
            time_permission = input("If hour not present, can we chose the same time period of the day, i.e. am and pm?(y/n)")
            if time_permission in {"y", "n"}:
                return time_permission
            print("Enter the correct option.")


slot = Slot()