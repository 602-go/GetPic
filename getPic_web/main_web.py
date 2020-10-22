import datetime
import time
import re
from flask import Flask,render_template,request,json,jsonify,url_for,redirect

import kss
from tobigs import *

class Keyword_Error(Exception):
    pass

app = Flask(__name__)

def hello():
    print('hello!!!!')


@app.route('/')  # 패턴
def home():  # 주소함수
    return render_template('index.html')

@app.route('/member')
def member():
    return render_template('member.html')

@app.route('/result', methods=['POST'])  # 문장분석해줌
def result():  # 주소함수
    # 0. initialize
    now = str(time.time())
    dloads_src = '/static/img/after_'+now+'.jpg'
    time_info = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    sentence = request.form['sentence']
    sentence = re.sub('\n', ' ', sentence)
    sentence = re.sub('\r', ' ', sentence)
    ###############################
    # 1. Get input text from user #
    ###############################
    input_text = kss.split_sentences(sentence)
    print(input_text)

    ######################
    # 2. Extract keyword #
    ######################
    keyword = get_keyword(input_text)
    print("추출된 키워드 > ", keyword)

    #######################
    # # 3. Image crawling #
    #######################
    if len(keyword) < 3:
        pass  # 예외처리
    else:
        image_link = get_crawlingImage(keyword, "PAPAGO_API_ID", "PAPAGO_API_PASSWORD", time_info, now)

        ##############################
        # 4. Predict sentiment label #
        ##############################
        sentiment_label = get_sentimentLabel(input_text, time_info)

        #####################
        # 5. Style transfer #
        #####################
        get_finalImage(image_link, sentiment_label, filename='after_'+now)

    return render_template('result.html',
                           sentence=sentence,
                           after_img='img/after_'+now+'.jpg',
                           dloads_src=dloads_src
                           )


# 이 코드를 메인으로 구동시 서버가동
if __name__ == '__main__':
    app.run(debug=True)
    device = torch.device("cpu")

