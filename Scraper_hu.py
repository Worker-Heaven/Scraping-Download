
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os
import csv
import configparser

import xlrd 

import mysql.connector

class Scrape:
  site_url = 'https://kozzetetelek.mnb.hu/en/short_selling/lekerdezo'
  download_path = 'lekerdezo.xlsx'
  chromedriver_path = ''
  time_limit = 20

  def read_config(self):
    config = configparser.ConfigParser()
    config.read('config.ini')

    self.chromedriver_path = config['DEFAULT']['driver_path']

  def load_chrome_driver(self):
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : os.getcwd()}
    chromeOptions.add_experimental_option("prefs",prefs)

    self.driver = webdriver.Chrome(executable_path=self.chromedriver_path, options=chromeOptions)
    self.driver.implicitly_wait(30)

  def download_wait(self):
    cwd = os.getcwd()
    seconds = 0
    dl_wait = True

    while dl_wait and seconds < self.time_limit:
      time.sleep(1)
      dl_wait = False
      files = os.listdir(cwd)

      print (files)
      for fname in files:
        if fname.endswith('.crdownload'):
          dl_wait = True
        else:
          dl_wait = False

      seconds += 1
    print ('second', seconds)
    return seconds

  def handle_csv(self):
    wb = xlrd.open_workbook(self.download_path) 
    sheet = wb.sheet_by_index(0)


  def run(self):
    self.read_config()
    self.load_chrome_driver()

    self.driver.get(self.site_url)

    print ('site is loading...')

    acceptBtns = self.driver.find_elements_by_xpath("//input[@id='acceptdisclaimer']")
    if len(acceptBtns) > 0:
      acceptBtns[0].send_keys("\n")

    downloadBtns = self.driver.find_elements_by_xpath("//input[@type='button' and @value='Export']")
    if len(downloadBtns) > 0:
        downloadBtns[0].send_keys("\n")

    seconds = self.download_wait()

    # NOTE: if download correctly
    if (seconds < self.time_limit):
      # self.handle_csv()
      # os.remove(self.download_path)
      self.driver.quit()

task = Scrape()
task.run()