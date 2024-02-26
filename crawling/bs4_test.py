from bs4 import BeautifulSoup
import pandas as pd
from requests import get
import time

base_url = "https://search.naver.com/search.naver?where=blog&sm=tab_opt&query=" #부동
query = "교육" # 부동
start = 1 # 동
url = f"{base_url}{query}&start={start}"
response = get(url)
soup = BeautifulSoup(response.text, 'html.parser')

detail = []
title = []
link = []

count = len(soup.find_all('div', class_ = "total_wrap api_ani_send"))


while True:
    if response.status_code == 200:
        if count == 29:
            basic = soup.find_all('div', class_ = "total_wrap api_ani_send")
            for i in basic:
                detail.append(i.find('div', class_ = "api_txt_lines dsc_txt").text)
                title.append(i.find('div', 'total_area').find_all('a')[5].get_text())
                link.append(i.find('div', 'total_area').find_all('a')[5]['href'])
            start+=30
            url = f"{base_url}{query}&start={start}"
            response = get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            time.sleep(2)
        else :
            basic = soup.find_all('div', class_ = "total_wrap api_ani_send")
            for i in basic:
                detail.append(i.find('div', class_ = "api_txt_lines dsc_txt").text)
                title.append(i.find('div', 'total_area').find_all('a')[5].get_text())
                link.append(i.find('div', 'total_area').find_all('a')[5]['href'])
            break
            
        
    else :
        print("접속불가")
        break
    
    
result = {
     '제목' : title,
        '내용' : detail,
        '링크' : link
    }
df_result = pd.DataFrame(result)
print(df_result)