import requests
from bs4 import BeautifulSoup
import re
for year in range(2018,2023):
    url = 'https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'.format(year)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    images = soup.find_all('img',attrs = {'class':'thumb_img'})

    for idx, image in enumerate(images):
        # print(image['src'])
        # if 'kakao' in image:
        #     image
        image_url = image['src']
        # if image_url.startswith('https:'):
        #     print(image_url)
        # else:
         #     print(f"https:{image_url}") #이건 내 코드
        if image_url.startswith('//'):
            image_url = 'https:' + image_url

        print(image_url)
        img_res = requests.get(image_url)
        img_res.raise_for_status()

        # 파일 만들어내는 로직
        with open("movie_{}_{}.jpg".format(year, idx+1),'wb') as f:
            f.write(img_res.content)
        if idx >= 4:
            break