#Slot Booking Script
#SBS 1.2
#Book two slots at the same time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

t420="C:\\Users\\"
t69="\\AppData\\Local\\Google\\Chrome\\User Data"
username=input("User account name in PC:")
profilepathtemp = t420 + username + t69
choice=input("Default Time 8 o'clock or Custom time(d/c):")

if choice in {"d", "D"}:
    temptime="20:00:01"
    print("Booking Time set as", temptime)
elif choice in {"c", "C"}:
    print("Slot opening time in 24 Hour format")
    hr=input("Hour(HH):")
    min=input("Minute(MM):")
    sec="01"
    temptime=str(hr + ":" + min + ":" + sec)
    print("Custom Booking Time set as", temptime)
else:
    print("The input must only be 'd' or 'c'")

link=input("Link of level/slot page that want to be booked-1 (First slot):")
link2=input("Link of level/slot page that want to be booked-2 (Third slot):")

if __name__=='__main__':
    stop_time = temptime
    while 1:
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
    profile_name = "Default"
    options.add_argument(f"--user-data-dir={profile_path}")
    options.add_argument(f"--profile-directory={profile_name}")

    Service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=Service, options=options)

    driver.get(link)

    driver.implicitly_wait(2)

    input_element = driver.find_element(By.CSS_SELECTOR, '.bg-primary.p-2.text-md.w-full.text-white.tracking-wider.rounded.mt-4')
    input_element.click()

    input_element1 = driver.find_element(By.CSS_SELECTOR, '.css-8mmkcg')
    input_element1.click()

    input_element2 = driver.find_element(By.CSS_SELECTOR, '.css-d7l1ni-option')
    input_element2.click()
    
    input_element3 = driver.find_element(By.CSS_SELECTOR, '.bg-primary.p-2.text-md.w-full.text-white.tracking-wider.rounded.mt-2')
    input_element3.click()

    # Open a new tab
    driver.execute_script("window.open('');")

    # Switch to the new tab and open another URL
    driver.switch_to.window(driver.window_handles[1])
    driver.get(link2)
    time.sleep(1)

    #Special thanks to Youtube, GeeksforGeeks and ChatGPT for this marvelous SBS 1.2
    
    # Click the 3rd element
    input_element6 = driver.find_element(By.CSS_SELECTOR, '.bg-primary.p-2.text-md.w-full.text-white.tracking-wider.rounded.mt-4')
    input_element6.click()

    input_element16 = driver.find_element(By.CSS_SELECTOR, '.css-8mmkcg')
    input_element16.click()

    elements2025 = driver.find_elements(By.CLASS_NAME, "css-10wo9uf-option")

    print("Total elements found:", len(elements2025))

    third_element = elements2025[1]
    
    # Click the 3rd element
    third_element.click()

    input_element36 = driver.find_element(By.CSS_SELECTOR, '.bg-primary.p-2.text-md.w-full.text-white.tracking-wider.rounded.mt-2')
    input_element36.click()

    time.sleep(10)

    driver.quit()