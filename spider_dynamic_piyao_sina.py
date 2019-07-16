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

item =[]
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

#逐渐滚动浏览器窗口，令ajax逐渐加载
for i in range(0,100):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    i += 1
    time.sleep(4)

number_s=[]
title_s=[]
for i in range(1,100):

    time =  driver.find_element_by_xpath('//div[@class="zy_day" and position()='+str(i)+']/div[@class="day_date"]')
    time = time.text
    print(time)
    titles=driver.find_elements_by_xpath('//div[@class="zy_day" and position()='+str(i)+']/div[@class="day_date"]/following-sibling::ul//div[@class="left_title"]')
    numbers=driver.find_elements_by_xpath('//div[@class="zy_day" and position()='+str(i)+']/div[@class="day_date"]/following-sibling::ul//div[@class="like_text"]')
    for i in titles:
        title_s.append(i.text)
    for j in numbers:
        number_s.append(j.text)

    z = zip(title_s,number_s)
    for title ,number in z:
        dic={}
        dic['title'] = title
        dic['time'] = time
        dic['number'] = int(number)
        print(number)
        item.append(dic)

driver.quit()
sorted(item,key=lambda x:x['number'],reverse=False)
print("谣言排名前10的依次是：",end="\n")
for i in item[:10]:
    print("谣言：",'\t',i['title'],'\t',"点赞数：",'\t',i['number'],'\t',"时间：",'\t',i['time'],end='\n')