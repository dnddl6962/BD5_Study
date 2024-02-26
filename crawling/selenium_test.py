from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from requests import get
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
from bs4 import BeautifulSoup


options = Options()
#options.add_argument("--no-sandbox")
#options.add_argument("--disable-dev-shm-usage") 
options.add_experimental_option("detach", True) #꺼지는거 막기
options.add_experimental_option("excludeSwitches", ["enable-automation"]) #경고문 없애기

driver = webdriver.Chrome(options=options)
keyword = '서울 종로구 어학원'
kakao_map_search_url = f"https://map.kakao.com/?q={keyword}"

driver.get(kakao_map_search_url)
driver.get(kakao_map_search_url)



list1 = []  # 결과물이 저장되는 리스트
i = 1
page = 1

while True:
    try:
        title = driver.find_element(by='xpath', value=f'//*[@id="info.search.place.list"]/li[{i}]/div[3]/strong/a[2]').text
        addr = driver.find_element(by='xpath',value = f'//*[@id="info.search.place.list"]/li[{i}]/div[5]/div[2]/p[1]').text
        list1.append([title, addr])
        print(title)
        print(addr)
        print(page)
        i+=1
    except:
        if driver.find_element(by='xpath',value = f'//*[@id="info.search.place.more"]').is_displayed():
            driver.execute_script("arguments[0].click();", driver.find_element(by='xpath',value = f'//*[@id="info.search.place.more"]'))
            time.sleep(5)
            page +=1
            i = 1
            continue
        elif driver.find_element(by='xpath',value = f'//*[@id="info.search.page"]/div').is_displayed():
            driver.execute_script("arguments[0].click();", driver.find_element(by='xpath',value = f'//*[@id="info.search.page.no{page}"]'))
            page += 1
            i = 1
            time.sleep(5)
            continue
        elif (page % 5 == 1):
            time.sleep(5)
            driver.execute_script("arguments[0].click();", driver.find_element(by='xpath',value = f'//*[@id="info.search.page.next"]'))
            page += 1
            i = 1
            time.sleep(5)
            continue
            