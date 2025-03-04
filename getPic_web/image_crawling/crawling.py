from selenium import webdriver
import time
from bs4 import BeautifulSoup
import os
import sys
import urllib.request
import requests
import nltk
import numpy as np
import random
import datetime
nltk.download('punkt')

class Crawling:
    def __init__(self, kor_keyword, client_id, client_secret):
        self.kor_keyword = kor_keyword      # 문장에서 추출한 키워드 (리스트)
        self.eng_keyword = []               # 한글 키워드를 파파고 API 이용해 번역한 결과
        self.client_id = client_id          # 파파고 API 아이디
        self.client_secret = client_secret  # 파파고 API 인증번호
        self.links = []                     # 크롤링한 이미지의 주소
        self.caps = []                      # 크롤링한 이미지의 캡션

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(r'C:\Users\kmmnj\Desktop\workspace\getPic_web\image_crawling\chromedriver.exe', options=options) # edit


    def get_eng_keyword(self):
        for keyword in self.kor_keyword:
            data = {'text': keyword,
                    'source': 'ko',
                    'target': 'en'}
            url = "https://openapi.naver.com/v1/papago/n2mt"
            header = {"X-Naver-Client-Id": self.client_id,
                      "X-Naver-Client-Secret": self.client_secret}
            response = requests.post(url, headers=header, data=data)
            rescode = response.status_code

            if rescode == 200:
                t_data = response.json()
                self.eng_keyword.append(str(t_data['message']['result']['translatedText']).lower())
            else:
                print("Error Code:", rescode)
        print(self.eng_keyword)

    def getting_link(self):
        pageString = self.driver.page_source
        bs_content = BeautifulSoup(pageString, "lxml")
        img_context = bs_content.find_all(name="div", attrs={"class": "nDTlD"})[0:100]
        # 100 images - but keep in mind that some does not give links, and also some links do not have as much as 100

        img_link = []
        img_cap = []
        for i in range(0, len(img_context)):
            imglist = img_context[i].select('img')
            if len(imglist) == 0:
                pass
            else:
                # getting link
                words = str(imglist).split()
                matchers1 = ['src']
                matching1 = [s for s in words if any(xs in s for xs in matchers1)]
                img_link.append(matching1[0][5:len(matching1[0]) - 1])

                # getting captions
                words2 = str(imglist).split('=')
                caption = words2[1][1:-7]
                img_cap.append(caption)
        return (img_link, img_cap)

    def scrolling_added(self):
        # initializing
        SCROLL_PAUSE_TIME = 2
        img_links = []
        img_caps = []

        for _ in range(10):  # edit
            img_link, img_cap = self.getting_link()
            img_links.extend(img_link)
            img_caps.extend(img_cap)

            # # Get scroll height
            # last_height = self.driver.execute_script("return document.body.scrollHeight")
            # # Scroll down to bottom
            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(SCROLL_PAUSE_TIME)
            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
            # time.sleep(SCROLL_PAUSE_TIME)
            #
            # # Calculate new scroll height and compare with last scroll height
            # new_height = self.driver.execute_script("return document.body.scrollHeight")
            # if new_height == last_height:
            #     break
            # last_height = new_height
        return (img_links, img_caps)

    def crawling_image(self):
        for i in range(0, 2):
            url = 'https://unsplash.com/s/photos/' + self.eng_keyword[i]
            self.driver.get(url)
            time.sleep(1)

            img_links, img_caps = self.scrolling_added()
            # print(img_links, img_caps)
            self.links.extend(img_links)
            self.caps.extend(img_caps)
        self.driver.close()

    # def save_image(self, time_info):
    #     # get jaccard similarity between keyword and caption (incomplete)
    #     caps_keywords = [nltk.word_tokenize(cap) for cap in self.caps]
    #     jaccard_sim = [len(set(self.eng_keyword) & set(cap_keyword)) / len(set(self.eng_keyword) | set(cap_keyword)) for cap_keyword in caps_keywords]
    #     # index of top 5 jaccard sim
    #     candidate_index = np.argsort(jaccard_sim)[-5:]
    #     # random sampling
    #     pick_index = random.choice(candidate_index)
    #     # save image
    #     link = f"static/img/before_{time_info[:-3]}.jpg"
    #     urllib.request.urlretrieve(self.links[pick_index], link)
    #     return link

    def save_image(self, time_info, now):
        # get jaccard similarity between keyword and caption (incomplete)
        caps_keywords = [nltk.word_tokenize(cap) for cap in self.caps]
        jaccard_sim = [len(set(self.eng_keyword) & set(cap_keyword)) / len(set(self.eng_keyword) | set(cap_keyword)) for cap_keyword in caps_keywords]
        # index of top 5 jaccard sim
        candidate_index = np.argsort(jaccard_sim)[-5:]
        # random sampling
        pick_index = random.choice(candidate_index)
        # save image
        link = "static/img/before_{}.jpg".format(now)
        urllib.request.urlretrieve(self.links[pick_index], link)
        return link


