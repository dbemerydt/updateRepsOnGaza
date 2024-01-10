import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import pickle

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time
from datetime import datetime

# Get today's date
today_date = datetime.today().strftime('%Y-%m-%d')

# Convert today's date to a string
date_string = str(today_date)

# File path where the text file is stored
file_path = 'messageBody.txt'

# Loading the contents of the text file as a string
with open(file_path, 'r') as file:
    body = file.read()

df = pd.read_csv('news.csv')

result = ''
for _, row in df.iterrows():
    values = row.values  # Get values of each row as a list
    result += '\n'.join(map(str, values))  # Join values with new lines
    result += '\n\n'  # Add a blank line after each row's information

# Trim trailing new line, if needed
result = result.rstrip('\n')

url = 'https://www.hickenlooper.senate.gov/email-john/#contact-form-emailJohn'
# Download and install the Chrome driver
chrome_service = ChromeService(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options = chrome_options, service=chrome_service)
driver.get(url)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# iframe_element = driver.find_element(By.TAG_NAME, "iframe")

# driver.switch_to.frame(iframe_element)

wait = WebDriverWait(driver, 10)
# zip5 = wait.until(EC.presence_of_element_located((By.NAME, "zip5")))
# zip5.send_keys('80303')
# zip5.send_keys(Keys.ENTER)

prefix = wait.until(EC.presence_of_element_located((By.ID, "input_17_2")))
prefixDropdown = Select(prefix)
prefixDropdown.select_by_index(4)

# noReply = driver.find_element(By.ID, "ctl00_ctl09_ReplyChoice_1")
# noReply.click()

firstname = driver.find_element(By.ID, "input_17_3_3")
lastname = driver.find_element(By.ID, "input_17_3_6")
address = driver.find_element(By.ID, "input_17_5")
city = driver.find_element(By.ID, "input_17_7")
state = driver.find_element(By.ID, "input_17_8")
stateDropdown = Select(state)
stateDropdown.select_by_index(6)

zipcode = driver.find_element(By.ID, "input_17_9")
phone = driver.find_element(By.ID, "input_17_11")
email = driver.find_element(By.ID, "input_17_10")
emailV = driver.find_element(By.ID, "input_17_10_2")

topic = driver.find_element(By.ID, "input_17_17")
topicDropdown = Select(topic)
topicDropdown.select_by_index(17)

subject = driver.find_element(By.ID, "input_17_18")
comment = driver.find_element(By.ID, "input_17_14")

# File path where the pickle file is stored
file_path = 'info.pickle'

# Loading data from the pickle file into a dictionary
with open(file_path, 'rb') as file:
    info = pickle.load(file)

firstname.send_keys(info['firstname'])
lastname.send_keys(info['lastname'])
address.send_keys(info['address'])
city.send_keys(info['city'])
zipcode.send_keys(info['zipcode'])
phone.send_keys(info['phone'])
email.send_keys(info['email'])
emailV.send_keys(info['email'])
subject.send_keys(info['subject']+ date_string)

comment.send_keys('Dear Senator Hickenlooper, \n'+body+'\n'+result)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# submit = driver.find_element(By.ID, 'gform_submit_button_17')
# submit.click()

time.sleep(120)



