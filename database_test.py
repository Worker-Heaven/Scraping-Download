from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import mysql.connector
import time
import csv
cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='test')
cursor = cnx.cursor()

def get_data(data):
  if len(data) > 0:
    return data[0].text
  else:
    return 'NaN'

def scrape_data(driver):
  time.sleep(1)
  name = driver.find_element_by_xpath("//h1[@class='section-hero-header-title']").text
  print ('name', name)
  ratings = driver.find_elements_by_xpath("//span[@class='section-star-display']")
  rating = get_data(ratings)
  print ('rating', rating)
  reviews = driver.find_elements_by_xpath("//li[@class='section-rating-term']//button[@class='widget-pane-link']")
  review = get_data(reviews)
  print ('review', review)
  addresses = driver.find_elements_by_xpath("//div[@data-section-id='ad']//span[@class='section-info-text']//span[@class='widget-pane-link']")
  address = get_data(addresses)
  print ('address', address)
  pluscodes = driver.find_elements_by_xpath("//div[@data-section-id='ol']//span[@class='section-info-text']//span[@class='widget-pane-link']")
  pluscode = get_data(pluscodes)
  print ('pluscode', pluscode)
  websites = driver.find_elements_by_xpath("//div[@data-section-id='ap']//span[@class='section-info-text']//span[@class='widget-pane-link']")
  website = get_data(websites)
  print ('website', website)
  phones = driver.find_elements_by_xpath("//div[@data-section-id='pn0']//span[@class='section-info-text']//span[@class='widget-pane-link']")
  phone = get_data(phones)
  print ('phone', phone)
  photoUrl = driver.find_elements_by_xpath("//div[@class='section-image-pack-image-container']//img")[0].get_attribute('src')
  print ('photoUrl', photoUrl)
  
  # ################# inserting data into mysql table
  
  add_apartment = ("INSERT INTO apartments "
               "(name, rating, review, address, pluscode, website, phone, photoUrl) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
  data_apartment = (name, rating, review, address, pluscode, website, phone, photoUrl)
  cursor.execute(add_apartment, data_apartment)
  cnx.commit()
  print(cursor.rowcount, "record inserted.")
 
  # #################
  with open('./result.csv', 'a+') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow([name, rating, review, address, pluscode, website, phone, photoUrl])

  backBtn = driver.find_element_by_xpath("//button[contains(@class, 'section-back-to-list-button')]")
  backBtn.send_keys("\n")
  time.sleep(1)


# constants for the app
SITE_URL = 'https://maps.google.com/'
download_path = './'
chromedriver_path = "./chromedriver"


with open('result.csv', 'w') as csvfile:
  writer = csv.writer(csvfile)

  writer.writerow(['name', 'rating', 'review', 'address', 'plus code', 'website', 'phone', 'photoUrl'])

# set up chrome options
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : download_path}
chromeOptions.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(executable_path=chromedriver_path, options=chromeOptions)
driver.implicitly_wait(30)

# Open the website
driver.get(SITE_URL)

print ('loading...')

# button = driver.find_element_by_xpath("//button/span[contains(text(), '(.csv)')]")

searchInput = driver.find_element_by_id('searchboxinput')
searchInput.send_keys("apartments near Scotland, UK")

searchButton = driver.find_element_by_id("searchbox-searchbutton")
searchButton.send_keys("\n")


while (1):
  for index in range(20):
    time.sleep(1)

    try:
      items = driver.find_elements_by_xpath("//div[@class='section-result']")
    except NoSuchElementException:
      driver.close()

    items[index].send_keys("\n")
    scrape_data(driver)

  time.sleep(2)
  driver.find_element_by_xpath("//button[@id='n7lv7yjyC35__section-pagination-button-next']").send_keys("\n")
cursor.close()
cnx.close()
