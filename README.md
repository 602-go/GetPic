# GetPic

**presented at [The 10th Tobigs Conference](https://user-images.githubusercontent.com/68496320/94992557-c19e3800-05c5-11eb-9e02-aafe3958e23b.jpg) in July 2020**

<table>
  <tr>
    <td align="center"><img src="https://user-images.githubusercontent.com/68496320/94986893-60fb0500-059d-11eb-9a4f-7d7612ef79a2.png" width="500px;" alt=""/></a></td>
  </tr>
</table>


---

## Table of Contents
[1. About getPic](#1-about-getPic)
  - [Example (ChatBot)](#example-chatbot)
  - [Example (Web)](#example-web)
[2. ChatBot](#2-chatbot)
  - [2.0. Install](#20-install)
  - [2.1. Test in Colab](#21-test-in-colab)
[3. Web](#3-web)
  - [3.0. Install](#30-install)
  - [3.1. At the Anaconda Prompt](#31-at-the-anaconda-prompt)
  - [3.2. At the PyCharm](#32-at-the-pycharm)
[4. Contributing](#4-contributing)
[5. Links](#5-links)
  

---

## 1. About getPic

**getPic** is a service that create illustration based on the input writing.
<br/>
The illustration is made based on the writing's context and emotion.
<br/>
getPic is a project developed by ToBigs Team3 using [KoBERT](https://github.com/SKTBrain/KoBERT/blob/master/README.md), Komoran, [Kwaii](https://github.com/kakao/khaiii.git), [TextRank](https://github.com/lovit/textrank/tree/master/textrank), [Fast-style Transfer](https://hoya012.github.io/blog/Fast-Style-Transfer-Tutorial/), etc.
<br/>
**getPic** is both available in **Web** and **Chatbot**.
So feel free to try!

> **getPic**은 입력 글의 내용과 감정에 어울리는 그림을 만들어줍니다.<br/>
이는 투빅스 제10회 컨퍼런스 3팀으로 참여한 작품이며, [KoBERT](https://github.com/SKTBrain/KoBERT/blob/master/README.md), Komoran, [Kwaii](https://github.com/kakao/khaiii.git), [TextRank](https://github.com/lovit/textrank/tree/master/textrank), [Fast-style Transfer](https://hoya012.github.io/blog/Fast-Style-Transfer-Tutorial/) 등을 사용합니다.<br/>
**웹**과 **챗봇**, 두 가지 방법으로 구현되어 있으니 참조 바랍니다.


#### Example (ChatBot)

<table>
  <tr>
    <td align="center"><img src="https://user-images.githubusercontent.com/68496320/94987601-6f97eb00-05a2-11eb-9116-c2c3b378ea41.jpg" width="500px;" alt=""/></a></td>
      <td align="center"><img src="https://user-images.githubusercontent.com/68496320/94987604-71fa4500-05a2-11eb-9aea-8651b377dd93.jpg" width="500px;" alt=""/></a></td>
  </tr>
</table>

You can freely download the resulted image :) <br/>
완성된 이미지를 자유롭게 저장하여 활용하세요 :)

#### Example (Web)

<table>
  <tr>
    <td align="center"><img src="https://user-images.githubusercontent.com/68496320/94986606-08c30380-059b-11eb-8b4b-6800f304aba2.png" width="700px;" alt=""/></a></td>
  </tr>
  <tr>
    <td align="center"><img src="https://user-images.githubusercontent.com/68496320/94986607-09f43080-059b-11eb-97af-aefc53af45bd.png" width="700px;" alt=""/></a></td>
  </tr> 
</table>

You can freely download the resulted image :) <br/>
완성된 이미지를 자유롭게 저장하여 활용하세요 :)

---

  
## 2. ChatBot

#### 2.0. Install

- Get access to [the drive](https://drive.google.com/drive/u/1/folders/1qkN8eAyB-1318YG-4d-BpyslDmhI23dI), download `bert_weight.pth` file, and put the file into the location `getPic_chatbot/weight/`

- [이 드라이브](https://drive.google.com/drive/u/1/folders/1qkN8eAyB-1318YG-4d-BpyslDmhI23dI)에서 `bert_weight.pth` 파일을 다운로드 받아 `getPic_chatbot/weight/` 경로에 넣어주시기 바랍니다.

#### 2.1. Test in Colab
- We recommend using GPU in Colab. You can change the runtime type by :[Runtime]-[Change runtime type]-[GPU] 

- Colab에서 [런타임] - [런타임 유형 변경] - 하드웨어 가속기(GPU) 사용을 권장합니다.

- `test.ipynb`: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/602-go/getPic/blob/master/getPic_chatbot/test.ipynb)

---

## 3. Web

#### 3.0. Install

- Get access to [the drive](https://drive.google.com/drive/u/1/folders/1qkN8eAyB-1318YG-4d-BpyslDmhI23dI), download `bert_weight.pth` file, and put the file into the location `getPic_web/weight/`

- [이 드라이브](https://drive.google.com/drive/u/1/folders/1qkN8eAyB-1318YG-4d-BpyslDmhI23dI)에서 `bert_weight.pth` 파일을 다운로드 받아 `getPic_web/weight/` 경로에 넣어주시기 바랍니다.

#### 3.1. At the Anaconda Prompt
- Create virtual environment
```sh
conda create -n virtual_environment_name
```
- Activate virtual environment
```sh
conda activate virtual_environment_name
```
- Clone and install requirements
```sh
git init
git config core.sparseCheckout true
git remote add -f origin https://github.com/602-go/getPic.git
echo "getPic_web" >> .git/info/sparse-checkout
git pull origin master
cd getPic_web
pip install -r requirements.txt
```

#### 3.2. At the PyCharm
- Activate virtual environment
```python
conda activate virtual_environment_name
```
- Execution
```python
python main_web.py
```
---

## 4. Contributing

<table>
  <tr>
    <td align="center"><a href="https://github.com/yunkio"><img src="https://user-images.githubusercontent.com/48192546/94985703-c4803500-0593-11eb-8912-341bf38e9fa4.jpg" width="100px;" alt=""/><br /><sub><b>Kio</b></sub> </a><br /><a href="" title="Email: yko22222@gmail.com ">📧</a></td>
      <td align="center"><a href="https://github.com/hyo-eun-kim"><img src="https://user-images.githubusercontent.com/48192546/94985814-a961f500-0594-11eb-81e0-ca1b0985adcf.jpg" width="100px;" alt=""/><br /><sub><b>Jane</b></sub></a><br /><a href="" title="Email: heun7410@gmail.com ">📧</a></td>
      <td align="center"><a href="https://github.com/KimHyunsun"><img src="https://user-images.githubusercontent.com/48192546/94985822-b0890300-0594-11eb-93a6-0d7965ea55dc.jpg" width="100px;" alt=""/><br /><sub><b>Sun</b></sub></a><br /><a href="" title="Email: hyunsun.kim0211@gmail.com ">📧</a></td>
    <td align="center"><a href="https://github.com/kmmnjng528"><img src="https://user-images.githubusercontent.com/48192546/94985889-28572d80-0595-11eb-98df-301edd4b764d.jpg" width="100px;" alt=""/><br /><sub><b>Ellie</b></sub></a><br /><a href="" title="Email: alswjd7950@naver.com ">📧 </a></td>
    <td align="center"><a href="https://github.com/gyeong707"><img src="https://user-images.githubusercontent.com/48192546/94985892-2db47800-0595-11eb-80dd-1f053acc0fc9.jpg" width="100px;" alt=""/><br /><sub><b>Anna</b></sub></a><br /><a href="" title="Email: kang9260@naver.com ">📧 </a></td>
    <td align="center"><a href="https://github.com/602-go"><img src="https://user-images.githubusercontent.com/48192546/94985894-3016d200-0595-11eb-9159-5db2eb4de0c5.jpg" width="100px;" alt=""/><br /><sub><b>Julia</b></sub></a><br /><a href="" title="Email: ygkoh602@gmail.com ">📧 </a></td>
  </tr>
</table>

---

## 5. Links

If you need more details about our project, visit [DataMarket](http://www.datamarket.kr/xe/board_pdzw77/67650) and look how we developed our project!

프로젝트에 관한 더욱 자세한 정보를 원하시면 [데이터마켓 공식 홈페이지](http://www.datamarket.kr/xe/board_pdzw77/67650)를 참고해주시기 바랍니다.


---
