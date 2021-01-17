#!/usr/bin/env python
# coding: utf-8

# In[81]:


from selenium import webdriver
from bs4 import BeautifulSoup
import requests

#driver 객체 생성
driver = webdriver.Chrome('C:\webcrawlers\chromedriver_win32\chromedriver') #webdriver 를 설치한 후 경로를 붙여넣기


URL = "https://www.ediya.com/contents/drink.html#c" # 크롤링하고자하는 웹사이트의 URL
driver.get(URL)

searchbutton = driver.find_element_by_css_selector("a.line_btn") #selenium의 버튼 자동 클릭 코드
searchbutton.click()

for i in range(50): # 메뉴판 전체를 보여주도록 하는 반복문
    
        
    try:
        time.sleep(0.5) # 0.5초 대기하기 
        
        # 사족 #
        # 이디야의 코드가 어떻게 짜여 있는지 몰라도 0.1 초 미만으로 버튼이 눌리도록 하면 계속해서 같은 페이지만 참조하는 오류가 있다.
        # 아마도 DB 를 참조하기까지 걸리는 시간 동안 버튼이 계속 눌리도록 해서 인 것 같은데,
        # 새로운 정보가 전달되지를 않았으니 열리는 새 창은 계속 똑같은 카라멜 마끼아또만 보여주는 것 같다.
        # 물론 인간의 반응속도는 그 정도로 빠르진 않기 때문에 대기 시간을 약간 늘리자 정상적으로 참조하는 모습을 보여주었다.
        nextpage = driver.find_element_by_css_selector("a.line_btn") 
        nextpage.click()
    except: 
        print("데이터 수집 완료.")  # 버튼이 눌리지 않으면 = 메뉴판을 전부 열면 반복문을 종료시킨다.
        break                      # 이렇게 해서 나중에 신메뉴가 추가되었어도 참조할 수 있다.

html = driver.page_source # 이제 동적인 부분을 끝냈으니 정적으로 변한 웹페이지의 소스를 갖고온다.
soup = BeautifulSoup(html, 'html.parser') #html 코드를 파싱한다. 정확한건 구글 ㄱㄱ
result = soup.select('ul#menu_ul') # 각 메뉴판을 참조한다. 메뉴판에는 영양성분, 알레르기 정보 등 유용한 정보가 있었기에 딱히 사용하진 않지만 가져오도록 했다.
titles = soup.select('ul#menu_ul > li > a > span') # 특정하게 메뉴 이름만 참조한다.


for i in range(len(titles)): # 참조한 메뉴 이름의 리스트를 가지고 반복문을 돌린다.
    print(titles[i].text) # 메뉴판의 string 만 따로 떼서 출력한다.

driver.close() # 열린 문은 닫힐지어니


# In[ ]:




