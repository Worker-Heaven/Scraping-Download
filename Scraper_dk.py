
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# constants for the app
site_url = 'https://oasm.dfsa.dk/uk/searchresult.aspx?t=shortselling'
download_path = './stg_rsi_hu'
chromedriver_path = "E:/Utilities/chromedriver.exe"

# set up chrome options
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : download_path}
chromeOptions.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(executable_path=chromedriver_path, options=chromeOptions)
driver.implicitly_wait(30)

# Open the website
driver.get(site_url)

print ('site is loading...')

acceptBtns = driver.find_elements_by_xpath("//input[@id='acceptdisclaimer']")
if len(acceptBtns) > 0:
    acceptBtns[0].send_keys("\n")
    driver.implicitly_wait(30)

downloadBtns = driver.find_elements_by_xpath("//input[@type='button' and @value='Export']")
if len(downloadBtns) > 0:
    downloadBtns[0].send_keys("\n")



