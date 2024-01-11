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
    result += '\n'.join(map(str, values[:-1]))  # Join values with new lines
    result += '\n\n'  # Add a blank line after each row's information

# Trim trailing new line, if needed
result = result.rstrip('\n')

url = 'https://www.bennet.senate.gov/public/index.cfm/write-to-michael'
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

prefix = wait.until(EC.presence_of_element_located((By.ID, "field_6B982348-2EDF-496C-B4F6-2B46EC249BC2")))
prefixDropdown = Select(prefix)
prefixDropdown.select_by_index(15)


noReply = driver.find_element(By.ID, "field_170B7597-532D-4D58-B551-32915A884AC1_2")
noReply.click()

noNewsletter = driver.find_element(By.ID, "field_8BE704C6-EB27-4C1A-AC3D-F345B61214C3_2")
noNewsletter.click()

firstname = driver.find_element(By.ID, "field_52D32F87-EEB0-4B98-A147-18D485A91778")
lastname = driver.find_element(By.ID, "field_6E3E9E0C-4536-4943-86DC-C3EABE533E5D")
address = driver.find_element(By.ID, "field_1EBBDF6B-817C-4A20-883D-7DA26637C09C")
city = driver.find_element(By.ID, "field_92DAAF40-EA9E-473C-8A60-D879AA1A8845")
zipcode = driver.find_element(By.ID, "field_3F76B5F8-807F-4173-8ECD-A9B5C0C5D881")
phone = driver.find_element(By.ID, "field_5ED31C3E-6AEC-4987-9A4F-1F5641AE5075")
email = driver.find_element(By.ID, "field_045DB8F4-2432-4E7E-B04C-ACE2C164D7A9")


topic = driver.find_element(By.ID, "field_A06A01A2-51E9-4761-A6C2-FD52E837A6C4")
topicDropdown = Select(topic)
topicDropdown.select_by_index(13)


subject = driver.find_element(By.ID, "field_4F515802-2FFE-4D01-A28E-326A8627C3E1")
comment = driver.find_element(By.ID, "field_0F40B55B-8631-4AA2-8223-08DE119CD370")

noReply = driver.find_element(By.ID, "field_170B7597-532D-4D58-B551-32915A884AC1_2")
noReply.click()

noNewsletter = driver.find_element(By.ID, "field_8BE704C6-EB27-4C1A-AC3D-F345B61214C3_2")
noNewsletter.click()

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
subject.send_keys(info['subject']+ date_string)


comment.send_keys('Dear Representative Bennet, \n'+body+'\n'+result)

submit = driver.find_element(By.XPATH, '//*[@id="form_586CEC0E-021A-4B24-B64E-A937A9EE9C18"]/div[2]/input')
submit.click()

driver.close()



