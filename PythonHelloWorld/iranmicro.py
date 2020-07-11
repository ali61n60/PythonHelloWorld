from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time
#####################

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://onlineplus.mofidonline.com/login')
browser.maximize_window()


## Username
element = browser.find_element_by_id("txtusername")
element.send_keys("mfdonline2917928")

time.sleep(1)

## Password
element = browser.find_element_by_id("txtpassword")
element.send_keys("11980An0063441578*")

time.sleep(8)
login = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/multi-login/div/div[2]/div[1]/form/div[4]/div[1]/button")
time.sleep(1)

login.click()

time.sleep(16)
#########################

### Forosh Zagross

zagross = browser.find_element_by_xpath("/html/body/app-container/app-content/div/div/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/ul/li[1]")
zagross.click()
time.sleep(2)



select_forosh = browser.find_element_by_xpath("/html/body/app-container/app-content/div/div/div/div[3]/div[2]/div/div/widget/div/div/div/div[2]/send-order/div/div[1]/div[2]/div")
select_forosh.click()
time.sleep(1)

tedad = browser.find_element_by_xpath("/html/body/app-container/app-content/div/div/div/div[3]/div[2]/div/div/widget/div/div/div/div[2]/send-order/div/div[5]/div[1]/div/div[2]/input")
tedad.send_keys("10")
time.sleep(1)

gimat = browser.find_element_by_xpath("/html/body/app-container/app-content/div/div/div/div[3]/div[2]/div/div/widget/div/div/div/div[2]/send-order/div/div[5]/div[2]/div/div[2]/input")
gimat.send_keys("218178")
time.sleep(1)

#forosh = browser.find_element_by_xpath("/html/body/app-container/app-content/div/div/div/div[3]/div[2]/div/div/widget/div/div/div/div[2]/send-order/div/div[7]/div[2]/a/div")
#forosh.click()

#Edame = browser.find_element_by_xpath("/html/body/app-container/app-content/div/div/div/div[3]/div[2]/div/div/widget/div/div/div/div[2]/send-order/div/div[8]/div/div[2]/div[1]")
#Edame.click()



