from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import wget
import time
import sys
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

PATH = '/Users/kewos554321/Downloads/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/")
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'))
)
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
username.clear()
password.clear()
username.send_keys("kewos554321@yahoo.com.tw")
password.send_keys('gh00437805')
login.click()

search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
)
keyword = 'monicaaaaaa_s'
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)

search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[1]/h2'))
)
# driver.set_page_load_timeout(110)
path = os.path.join(keyword)
if not os.path.isdir(path): os.mkdir(path)
imgs = driver.find_elements_by_class_name('FFVAD')
count = 0
for img in imgs:
    save_as = os.path.join(path, keyword+'_'+str(count)+'.jpg')
    # print(img.get_attribute('src'))
    wget.download(img.get_attribute('src'), save_as)
 
    count+=1
time.sleep(5)
driver.quit()
