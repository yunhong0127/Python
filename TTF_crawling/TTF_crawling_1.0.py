from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

# connect
driver = webdriver.Chrome('/Users/yoonhongkim/Desktop/python work space/chromedriver/chromedriver90')
driver.get('https://shop347353094.taobao.com/search.htm?spm=a1z10.3-c.0.0.255731a3CfvY6Q&search=y&orderType=newOn_desc')

time.sleep(2+random.random())

# login
e = driver.find_elements_by_class_name('fm-text')[0]
e.send_keys('13206523203')
e = driver.find_elements_by_class_name('fm-text')[1]
e.send_keys('dboyb5142~')
e.send_keys(Keys.ENTER)