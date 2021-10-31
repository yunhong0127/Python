from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

# connect
driver = webdriver.Chrome('/Users/yoonhongkim/Desktop/python work space/instagram_bot/chromedriver/chromedriver90')
driver.get('https://www.instagram.com')

time.sleep(2+random.random())

# login
e = driver.find_elements_by_class_name('_2hvTZ')[0]
e.send_keys('ID')
e = driver.find_elements_by_class_name('_2hvTZ')[1]
e.send_keys('PW')
e.send_keys(Keys.ENTER)

time.sleep(4+random.random())

#popup
e = driver.find_elements_by_class_name('sqdOP')[1]
e.click()
e = driver.find_elements_by_class_name('HoLwm')[0]
e.click()

time.sleep(2+random.random())

# search
driver.get('https://www.instagram.com/explore/tags/여자코디/')

time.sleep(5+random.random())

# get first feed
xpath = "/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]"
driver.find_elements_by_xpath(xpath)[0].click()

time.sleep(5+random.random())

while True:
    # variable that detemines whether you like or pass
    do_like = False

    #좋아요 클릭
    #if do_like:
    #xpath = "//article//section/span/button"
    #driver.find_elements_by_xpath(xpath)[0].click()
    
    #time.sleep(5+random.random())

    # posts with too many likes are passed.
    if do_like:
        try:
            num_of_like = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/artical/div[3]/section[2]/div/div/button/span').text
            num_of_like = int(num_of_like)
            if num_of_like > 100:
                do_like = False
                print('post with %d likes is passed.' % num_of_like)
        except:
            pass

    # only like posts that you haven't liked yet
    if do_like:
        like = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section/span/button')
        try:
            alt = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[2]/div[1]/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div[1]/div/img').get_attribute("alt")
        except:
            try:
                alt = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[2]/div[1]/div[1]/div[1]/img').get_attribute("alt")
            except:
                alt = "video?"
        try:
            likeBtn = driver.find_element_by_xpath('//*[@aria-label="좋아요"]')
        except:
            break

    #comment
    if do_like:
        try:
            students = ['댓글']
            e = driver.find_elements_by_class_name('Ypffh')[0]
            e.click()
            e = driver.find_elements_by_class_name('Ypffh')[0]
            e.send_keys(random.choice(students))
            e.send_keys(Keys.ENTER)
        except:
            pass

    time.sleep(1.5+random.random())

    #get next feed
    xpath2 = "//a"
    el_list = driver.find_elements_by_xpath(xpath2)
    for el in el_list:
        if el.text == "다음":
            el.click()
            break
    time.sleep(2.5+random.random())
