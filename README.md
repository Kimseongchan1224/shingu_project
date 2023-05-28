# <div align=center>⭐AMAZON 리뷰 긍부정 예측분석⭐</div>
![amazon](https://user-images.githubusercontent.com/79899868/235655097-f163a37c-ec5c-4337-8c28-e230e1064586.png)

<div align=center>Amazon은 미국의 인터넷 플랫폼 기업으로, 세계 최대의 온라인 쇼핑몰 기업이자 세계 최대의 클라우드 컴퓨팅 서비스 기업이다.</div>

>[출처:로고](https://logos-world.net/amazon-logo/)&nbsp;/&nbsp;[출처:나무위키](https://namu.wiki/w/%EC%95%84%EB%A7%88%EC%A1%B4)
<div align=center>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/></a>
<img src="https://img.shields.io/badge/PyTorch-E34F26?style=flat-square&logo=PyTorch&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=Jupyter&logoColor=white"/></a>
</div><hr>

## 1.개요

### 1-1. 목적
온라인 쇼핑몰의 규모가 커져가는 요즘, 사람들이 남긴 리뷰를 분류하는 프로그램을 Mobile Bert를 활용하여 만들고자한다.
온라인 쇼핑몰의 리뷰를 알아서 분류하는 프로그램을 개발하여 소비자가 합리적으로 구매하는데 도움을 주고 쇼핑몰 판매자가 상품을 구상하는데 좋은 피드백을 얻을수 있고 
기업에서는 부정적인 댓글과 악성댓글을 분류해서 삭제하여 올바른 리뷰 문화가 생길 것이라 예측이 된다.

### 1-2.온라인 쇼핑몰의 영향력
온라인 쇼핑몰의 영향력은 어느 정도 일까? 오늘날 인터넷 쇼핑몰로 대표되는 전자상거래는 인터넷 사용인구의 급증과 기술의 발달을 통해 꾸준히 성장하고 있다. 인터넷 쇼핑몰 시장의 급속한 성장과 더불어 시장의 경쟁은 점차 심화되어가고 있으며, 이러한 치열한 경쟁 상황에서 경쟁우위를 확보하기 위해서 인터넷 쇼핑몰의 기술적 개선 외에도 소비자와 관계형성 및 유지를 위한 관계적 커뮤니케이션 환경의 필요성이 대두되고 있다. 그것 중 하나가 바로 리뷰이다. 

커머스 업계에서 고객 후기의 중요성이 커지고 있다. 아마존, 네이버 쇼핑, 쿠팡, 11번가와 같은 대형 오픈마켓 커머스들 또한 리뷰어 랭킹제 도입, 리뷰 항목 체계화, 파격적인 리워드 제공 등을 통해 나름의리뷰 시스템을 활발하게 구축하고 있다. 이에 발 맞춰 온라인 쇼핑몰이 사용하는 리뷰 솔루션 업체들 역시 서비스를 빠르게 고도화 중이다.이처럼 커머스들이 너 나 할 것 없이 리뷰 시스템에 투자하는 이유는 소비자 후기가 매출에 실질적인 영향을 주기 때문이다. ‘맥킨지앤드컴퍼니’의 조사에 따르면 실구매자의 후기는, 쇼핑몰의 추천보다 잠재소비자의 구매 결정에 10배 가량 높은 영향력을 행사한다고 한다. 리뷰의 중요성을 더 편하게 보기위해 아마존 리뷰데이터를 통해 긍부정 예측을 하고자 한다.

>[출처:유병관 교수](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01769129)&nbsp;/&nbsp;
>[출처:아시아투데이](https://www.asiatoday.co.kr/view.php?key=20200219010011433)&nbsp;/&nbsp;
>[출처:Kca.go.kr](https://www.kca.go.kr/home/board/download.domenukey=6101&fno=10014613&bid=00000146&did=1002001011)

### 1-3.예측분석 순서

![dtf](https://user-images.githubusercontent.com/79899868/235818872-71472c0f-fbb9-4364-8c67-ed5d504a5557.png)
1. 분석할 아마존 리뷰 데이터를 Kaggle에서 Excel 데이터을 확보를 합니다.
2. Excel 데이터를 pycham에서 인식할 수 있게 텍스트화 작업을 합니다.
3. python을 활용하여 텍스트 데이터를 학습시키는 작업 합니다.
4. 학습이 된 프로그램을 작동시켜 긍정과 부정으로 분류하는지 확인을 합니다.

>[로고](https://icon-icons.com/ko/%EC%95%84%EC%9D%B4%EC%BD%98/amazon-%EB%A1%9C%EA%B3%A0/169611)

## 2.데이터

[아마존 리뷰 데이터 @kaggle/DANIEL_IHENACHO](https://www.kaggle.com/datasets/danielihenacho/amazon-reviews-dataset)

### 2-1.원시데이터
| 데이터 | 구분 |
| --- | --- |
| `sentiments` | *부정적, 중립적, 긍정적 3가지로 데이터를 나타냅니다..* |
| `cleaned_review` | *텍스트 리뷰 데이터 입니다.* |
| `cleaned_review_length` | *텍스트 리뷰의 길이 입니다.(단어 갯수)* |
| `review_score` | *1부터5까지 점수를 나타냅니다* |<br>


| count| `sentiments` | `cleaned_review` |  `cleaned_review_length` | `review_score` |
| --- | --- | --- | --- | --- |
| 0 | positive | i wish would have gotten one earlier love it a... | 19 | 5 |
| 1 | neutral	  | i ve learned this lesson again open the packag...	 | 88 | 1 |
| 2 | neutral | it is so slow and lags find better option	 | 9 | 2 |
| 3 | neutral | roller ball stopped working within months of m... | 12 | 1 |
| 4 | neutral | i like the color and size but it few days out ...	 | 21 | 1 |
|... | ... | ... | ... | ... |
| 17335| positive | i love this speaker and love can take it anywh...	 | 30 | 5 |
| 17336 | positive | i use it in my house easy to connect and loud ... | 13 | 4 |
| 17337 | positive | the bass is good and the battery is amazing mu...	 | 41 | 5 |
| 17338 | positive | love it | 2 | 5 |
| 17339 | neutral | mono speaker	 | 2 | 5 |<br><br>

![onesi](https://github.com/Kimseongchan1224/shingu_project/assets/79899868/5a02640a-77b2-4600-9eb8-8c9e06b1a2c8)<br>

positive 긍정적, neutral  중립적, negative 부정적<br> 
sentiments에는 긍정, 중립, 부정의 3가지 데이터로 나뉜다 긍정적인 데이터가 50% 이상 차지하고 있다.<br> 
데이터를 학습시킬 때 중립의 데이터를 분배하거나 삭제가 필요하다.<br>
텍스트 리뷰 길이의 대한 도수분포표이다. 100개 이상의 단어를 사용한 데이터 삭제가 필요하다.<br>
review_score는 1~5까지 점수 데이터인데 5➡1➡4➡2➡3 순서로 5점이 제일 많다고 볼 수 있다.<br> 
5점으로 갈수록 대부분 긍정적인 리뷰인데 데이터 전반적으로 긍정적인 데이터가 많다고 볼 수 있다.<br> <br> 

### 2-2.가공데이터
| count| `sentiments` | `cleaned_review` |  `cleaned_review_length` | `review_score` |
| --- | --- | --- | --- | --- |
| 0 | negative | i loved this keyboard when first started using it but that didn... | 99 | 1 |
| 1 | positive | i not rating this one star because it is cute mouse and like...	 | 99| 4 |
| 2 | positive | i not rating this one star because it is cute mouse and like...	 | 99| 1 |
| 3 | positive | i really liked this mouse being able to charge it and not... | 99 | 5 |
| 4 | positive | i use this for when am showering and got it to replace bose...	 | 99 | 1 |
|... | ... | ... | ... | ... |
문장에 들어가는 단어의 길이가 100개 이상인 데이터를 제거함.
| count| `sentiments` | `cleaned_review` |  `cleaned_review_length` | `review_score` |
| --- | --- | --- | --- | --- |
| 0 | negative | i loved this keyboard when first started using it but that didn... | 99 | 1 |
| 1 | positive | i not rating this one star because it is cute mouse and like...	 | 99| 4 |
| 2 | positive | i not rating this one star because it is cute mouse and like...	 | 99| 1 |
| 3 | positive | i really liked this mouse being able to charge it and not... | 99 | 5 |
| 4 | positive | i use this for when am showering and got it to replace bose...	 | 99 | 1 |
|... | ... | ... | ... | ... |
