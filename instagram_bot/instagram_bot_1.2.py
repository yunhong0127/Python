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
e.send_keys('PW~')
e.send_keys(Keys.ENTER)

time.sleep(4+random.random())

#popup
e = driver.find_elements_by_class_name('sqdOP')[1]
e.click()
e = driver.find_elements_by_class_name('HoLwm')[0]
e.click()

time.sleep(2+random.random())

# Searches for posts that contain at least one tag belonging to tag2
# among the search results of tag1
tag1 = "운동스타그램"
tag2 = ["운동스타그램"]

# search tag1
driver.get('https://instagram.com/explore/tags/'+tag1)

time.sleep(5+random.random())

# get first feed
feed = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div/div/a')
feed.send_keys(Keys.ENTER)

time.sleep(5+random.random())

i = 0
while True:
    # variable that detemines whether you like or pass
    do_like = False

    # check if any of the tags belonging to tag2 are included
    for multi_tag in tag2:
        try:
            tag = driver.find_element_by_xpath('//*[@href="/explore/tags/%s/"]' % multi_tag)
            do_like = True
            break
        except:
            pass

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
    
    #
    if do_like:
        try:
            tag2 = ["소액","마켓","shop","재테크","쇼핑몰","매장","샵"]
            if tag2 in ('/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul'):
                do_like = False
                print('post with %d likes is passed.' % num_of_like)
        except:
            pass

    # only like posts that you haven't liked yet
    if ("좋아요 취소") in ('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span'):
                do_like = False
                print('post with %d likes is passed.' % num_of_like)
    else:
        pass

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

        if "여자코디" not in alt:
           like.send_keys(Keys.ENTER)
           print('%d like' % (i+1))
           i += 1
           if i >= 100:
               break
        time.sleep(2+random.random())

    #comment
    # if do_like:
    #     try:
    #         students = ['댓글']
    #         e = driver.find_elements_by_class_name('Ypffh')[0]
    #         e.click()
    #         e = driver.find_elements_by_class_name('Ypffh')[0]
    #         e.send_keys(random.choice(students))
    #         e.send_keys(Keys.ENTER)
    #     except:
    #         pass
    #     time.sleep(2+random.random())

    # get next feed
    nextFeed = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/a[2]')
    ac = ActionChains(driver)
    ac.move_to_element(nextFeed)
    ac.click()
    ac.perform()
    time.sleep(3+random.random())

print('total like : %d' % i)
