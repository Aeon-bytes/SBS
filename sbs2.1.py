#Slot Booking Script
#SBS 2.1
#Book two slots at the same time with am and pm

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
import json

class Slot:
    def __init__(self):
        t420="C:\\Users\\"
        t69="\\AppData\\Local\\Google\\Chrome\\User Data"
        SLEEP_TIME = 10
        username = os.getlogin()

        profilepathtemp = t420 + username + t69

        profile_id = self.get_profile(profilepathtemp)

        temptime = self.set_time()

        link=input("Link of level/slot page that want to be booked-1:")

        range_type = self.slot_range()

        while True:
            checklink = input("Do you want to book a slot 2(y/n): ")
            if (checklink in {"n", "N"}):
                break
            elif (checklink in {"y", "Y"}):
                link2=input("Link of level/slot page that want to be booked-2:")
                print("Make sure that the other slot is not at the same time")
                range_type2 = self.slot_range()
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
                self.slot_selection_type1(driver, range_type)

                input_element3 = driver.find_element(By.CSS_SELECTOR, '.bg-primary.p-2.text-md.w-full.text-white.tracking-wider.rounded.mt-2')
                input_element3.click()
                
            except NoSuchElementException:
                print("No options found.")
            


            if checklink in {"n", "N"}:
                time.sleep(SLEEP_TIME)
                driver.quit()
            else:
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[1])
                driver.get(link2)
                driver.implicitly_wait(0.5)
                
                input_element6 = driver.find_element(By.CSS_SELECTOR, '.bg-primary.p-2.text-md.w-full.text-white.tracking-wider.rounded.mt-4')
                input_element6.click()

                input_element16 = driver.find_element(By.CSS_SELECTOR, '.css-8mmkcg')
                input_element16.click()

                try:
                    self.slot_selection_type1(driver, range_type2)

                    input_element3 = driver.find_element(By.CSS_SELECTOR, '.bg-primary.p-2.text-md.w-full.text-white.tracking-wider.rounded.mt-2')
                    input_element3.click()

                except NoSuchElementException:
                    print("No options found.")

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

    def slot_range(self):
        while True:
            range_type = input("Enter the slot timings(am/pm/default):")
            if range_type in {"am", "pm", "default"}:
                return range_type
            print("Enter the correct character.")

    def convert_to_24_hour(self, time_):
        time_part, time_period = time_.split()
        
        hours = int(time_part.split(':')[0])
        
        if time_period.lower() == 'pm' and hours != 12:
            hours += 12
        elif time_period.lower() == 'am' and hours == 12:
            hours = 0
            
        return hours
    
    def slot_selection_type1(self, driver, range_type):

        if (range_type == "default"):
                input_element2 = driver.find_element(By.CSS_SELECTOR, '.css-d7l1ni-option')
                input_element2.click()
                return
        
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
            if (range_type == "am"):
                if hour < 12:
                    print(i["text"][13:21])
                    input_element2 = driver.find_element(By.CSS_SELECTOR, f'#{i["id name"]}')
                    input_element2.click()
                    return
                
            else:
                if hour >= 12:
                    print(i["text"][13:21])
                    input_element2 = driver.find_element(By.CSS_SELECTOR, f'#{i["id name"]}')
                    input_element2.click()
                    return
        
        print("NO Options found.")

slot = Slot()