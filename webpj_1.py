import re
import requests
from bs4 import BeautifulSoup
import time

#[오늘의 날씨]
# 흐림, 어제보다 00 높아요
# 현재 00 (최저 00/최고 00)
# 오전 강수확률 00%/ 오후 강수확률 00%

#미세먼지 00mg/m^2 좋음
#초미세먼지 00mg/m^2 좋음


def scrape_weather():
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8'
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    res = requests.get(url, headers= headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')
    # 흐림, 어제보다 00 높아요
    weather = soup.find('span',attrs={'class':'weather before_slash'}).get_text()
    yesterday = soup.find('div',attrs={'class':'temperature_info'}).find('span',attrs={'class':'temperature down'}).get_text()




    #현재 온도
    today_temperature = soup.find('div',attrs={'class':'temperature_text'}).find('strong').get_text()

    #최저/최고
    low_tem = soup.find('div',attrs={'class':'cell_temperature'}).find('span',attrs={'class':'lowest'}).get_text()
    high_tem = soup.find('div',attrs={'class':'cell_temperature'}).find('span',attrs={'class':'highest'}).get_text()

    #강수확률
    p1 = soup.find_all('span',attrs={'class':'weather_left'})[0].get_text()
    p2 = soup.find_all('span',attrs={'class':'weather_left'})[1].get_text()
    #미세먼지, 초미세먼지
    dust = soup.find_all('li',attrs={'class':'item_today level2'})[0].get_text().strip()
    super_dust = soup.find_all('li',attrs={'class':'item_today level2'})[1].get_text().strip()

    print('[오늘의 날씨는]')
    print(f'{weather} 어제보다 {yesterday}')
    print(f"{today_temperature}({low_tem}/{high_tem})")
    print(f"강수확률 {p1}{p2}")
    print(dust)
    print(super_dust)
if __name__ == "__main__":
    scrape_weather()



# [헤드라인 뉴스]
# 1. -------------
 #링크()
# 2

#3
def scrape_headline_news():
    url = 'https://news.naver.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')

    headline_news = soup.find_all('div',attrs={'class':'cjs_journal_wrap _item_contents'})
    print('\n[헤드라인 뉴스]')
    for idx, headline_new in enumerate(headline_news):
        title = headline_new.find('div',attrs= {'class':'cjs_t'}).get_text()
        link = headline_new.find('a')['href']

        print(f"{idx+1}.{title}")
        print(f"링크({link})")

        if idx == 2:
            break

if __name__ == "__main__":
    scrape_headline_news()


def scrape_it_news():
    url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105'
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')

    it_news = soup.find('div', attrs= {'class':'cluster_group _cluster_content'}).find_all('li',limit = 3)
    print('\n[IT 헤드라인 뉴스]')

    for idx, it_new in enumerate(it_news):
        title = it_new.find('div', attrs = {'class':'cluster_text'}).find('a', attrs = {'class':'cluster_text_headline nclicks(cls_sci.clsart)'}).get_text()
        link = it_new.find('a')["href"]
        print(f"{idx + 1}.{title}")
        print(f"링크({link})")

if __name__ == "__main__":
    scrape_it_news()


# [오늘의 영어 회화]
# (영어 지문)
# jason:~~~~~~~~
# kim : Well, I think....

# (한글 지문)
# jason: 어쩌구~
def scrape_English():
    url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english'
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    res = requests.get(url, headers= headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')


    # 영어지문 가져오기
    sentences = soup.find_all('div', attrs = {"id": re.compile("^conv_kor_t")})
    print('\n(영어 지문)')

    for sentence in sentences[len(sentences)//2:]:
        English_sentence = sentence.get_text().strip()
        print(English_sentence)

    time.sleep(3)
    print('\n(한글 지문)')

    for sentence in sentences[:len(sentences)//2]:
        korean_sentence = sentence.get_text().strip()
        print(korean_sentence)

if __name__ == "__main__":
    scrape_English()


