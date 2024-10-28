#Selenium Automation Script for Ebay v28.04.2023
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Browser
driver = webdriver.Chrome()
driver.get("https://www.ebay.co.uk/?mkcid=1&mkrid=710-53481-19255-0&siteid=3&campid=5338626673&toolid=20008&mkevt=1&customid=engbtopsitescurateana")
driver.maximize_window()
driver.implicitly_wait(30)

#Function for finding Samsung Phones
def find_samsung():
    samsung = []
    items = driver.find_elements(By.CLASS_NAME, "s-item__title")
    for item in items:
        if 'Samsung' in item.text:
            samsung.append(item.text)
    print(f"Samsung = {len(samsung)}/{len(items)}")

#Function for Next Page Navigation
def next_page():
    try:
        next = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="srp-river-results"]/ul/li[65]/div[2]/span/span/nav/a')))
        next.click()
    except:
        print("Failed Next Page")
        driver.quit()

#Search for Phones with Explicit Wait
try:
    search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gh-ac"]')))
    search.clear()
    search.send_keys("phone" + Keys.RETURN)
except:
    print("Failed Phone Search")
    driver.quit()

#Find Samsung Count then Next Page
find_samsung()
next_page()
find_samsung()

#Go back
driver.back()

#Close
time.sleep(5)
driver.quit()