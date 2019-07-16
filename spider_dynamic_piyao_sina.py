# -*- coding: utf-8 -*- 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
import time
import os
import re
import platform
from lxml import etree
from datetime import datetime

chrome_driver_path = ""
main_page_url ="http://piyao.sina.cn/"
if platform.system()=='Windows':
    chrome_driver_path = "chromedriver.exe"
elif platform.system()=='Linux' or platform.system()=='Darwin':
    chrome_driver_path = "./chromedriver"
else:
    print('Unknown System Type. quit...')



chrome_options = Options()
chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options, \
    executable_path=chrome_driver_path)
        
driver.get(main_page_url)
time.sleep(5)

item=[]
for i in range(1,10):
    titles=[]
    numbers=[] 
    time =  driver.find_element_by_xpath('//div[@class="zy_day" and position()='+str(i)+']/div[@class="day_date"]')
    print(time.text)
    titles.append(driver.find_element_by_xpath('//div[@class="zy_day" and position()='+str(i)+']/div[@class="day_date"]/following-sibling::ul//div[@class="left_title"]')
    numbers.append(driver.find_elements_by_xpath('//div[@class="zy_day" and position()='+str(i)+']/div[@class="day_date"]/following-sibling::ul//div[@class="left_like"]')
    number =[]
    for i in numbers:
        number.append(i.text())
    z = zip(titles,numbers)
    for title ,number in z:
        dic={}
        dic['title'] = title
        dic['time'] = time
        dic['number'] = number
        print(number)

        item.append(dic)

for i in item:
    i.number=int(i.number)





