import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('C:/Users/82109/nadocoding/chromedriver.exe')
browser.maximize_window()# 창최대화

url = 'https://flight.naver.com/'
browser.get(url) # 1. url로 이동

#2. 팝업창 없애기
browser.find_elements_by_class_name('btn')[2].click()
#xpath를 통해 이게 3번쨰 순서에 있는 버튼인 것을 알아냈어1
#__next > div > div.container.as_main > div.popup_travelclub > div > div.btns > button:nth-child(2)

#3. 가는날 선택클릭
begin_date = browser.find_element(By.XPATH, "//button[text() = '가는 날']")
begin_date.click()

# 이번 달 27,28일
# time.sleep(0.5)
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH,"//b[text()='27']")))
day27 = browser.find_elements(By.XPATH, "//b[text()='27']")
day27[0].click()
day31 = browser.find_elements(By.XPATH, "//b[text()='31']")
day31[0].click()

arrival = browser.find_element(By.XPATH,"//b[text()='도착']")
arrival.click()

# time.sleep(0.5)
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH,"//button[text() = '국내']")))
domestic = browser.find_element(By.XPATH, "//button[text() = '국내']")
domestic.click()

WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH,"//i[text()='제주국제공항']")))
jeju = browser.find_element(By.XPATH,"//i[text()='제주국제공항']")
jeju.click()

ticket = browser.find_element(By.XPATH,"//span[text()='항공권 검색']")
ticket.click()

#loading 시간 저 element가 나올때까지 기다리고 최대 30초 기다려줘
elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH,"//div[@class='domestic_Flight__sK0eA result']")))

