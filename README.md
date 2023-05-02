# <div align=center>AMAZON 리뷰 긍부정 예측분석</div>
![amazon](https://user-images.githubusercontent.com/79899868/235655097-f163a37c-ec5c-4337-8c28-e230e1064586.png)

<div align=center>Amazon은 미국의 인터넷 플랫폼 기업으로, 세계 최대의 온라인 쇼핑몰 기업이자 세계 최대의 클라우드 컴퓨팅 서비스 기업이다.</div>
<div align=center>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/></a>
<img src="https://img.shields.io/badge/PyTorch-E34F26?style=flat-square&logo=PyTorch&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=Jupyter&logoColor=white"/></a>
</div><hr>

## 문제정의
- 온라인 쇼핑몰의 규모가 커져가는 가운데 사람들이 남긴 리뷰를 알아서 분류하는 프로그램을 만들고 싶었다.
- 온라인 쇼핑몰의 리뷰를 알아서 분류하는 프로그램이 있으면 소비자가 합리적으로 구매하는데 큰 도움이 된다고 생각하였다.
- 쇼핑몰 판매자 입장에서는 상품을 구상하는 데에 좋은 피드백이 될 수 있고 기업 입장에서는 부정적인 댓글 중 악성 댓글을 알아서 처리해 주면 올바른 리뷰 문화가 생길 것이라고 생각하였다.

## 댓글의 영향력
리뷰의 영향력은 어느 정도일까? 급속히 변화 및 발전하는 온라인 환경에서 소비자들이 자발적으로 작성하고 공유하는 소비자 리뷰 정보는 시장에서의 정보 비대칭 문제를 해소할
수 있는 기제로 작동되기에 큰 의미를 지닌다. 특히 소셜 네트워크 커뮤니티, 개인 미디어 등 1인 기반 서비스를 중심으로 정보제공 플랫폼이 재편되고 있기에 소비자 리뷰가 미치는 영향력은 갈수록 커질 것으로
보인다. 

커머스 업계에서 고객 후기의 중요성이 커지고 있다. 아마존, 네이버 쇼핑, 쿠팡, 11번가와 같은 대형 오픈마켓 커머스들 또한 리뷰어 랭킹제 도입, 리뷰 항목 체계화, 파격적인 리워드 제공 등을 통해 나름의
리뷰 시스템을 활발하게 구축하고 있다. 이에 발 맞춰 온라인 쇼핑몰이 사용하는 리뷰 솔루션 업체들 역시 서비스를 빠르게 고도화 중이다.이처럼 커머스들이 너 나 할 것 없이 리뷰 시스템에 투자하는 이유는 소비자 후기가 
매출에 실질적인 영향을 주기 때문이다. ‘맥킨지앤드컴퍼니’의 조사에 따르면 실구매자의 후기는, 쇼핑몰의 추천보다 잠재소비자의 구매 결정에 10배 가량 높은 영향력을 행사한다고 한다.
>[출처:아시아투데이](https://www.asiatoday.co.kr/view.php?key=20200219010011433)<br>

## 예측분석 순서

![can](https://user-images.githubusercontent.com/79899868/235660196-9864d0ac-e9b1-4537-ba72-5bedfe42619f.png)
- 분석할 아마존 리뷰 데이터를 Kaggle에서 Excel 데이터 다운로드
- Excel 데이터를 pycham에서 인식할 수 있게 텍스트화 작업
- python을 활용하여 텍스트 데이터를 학습시키는 작업
- 학습이 된 프로그램을 작동시켜 긍정과 부정으로 분류하는지 확인
- 
## 데이터 미리보기

[아마존 리뷰 데이터 @kaggle/DANIEL IHENACHO](https://www.kaggle.com/datasets/advaypatil/youtube-statistics/versions/1?resource=download)

| 데이터 | 구분 |
| --- | --- |
| `sentiments` | *부정적, 중립적, 긍정적 3가지로 데이터를 나타냅니다..* |
| `cleaned_review` | *텍스트 리뷰 데이터 입니다.* |
| `cleaned_review_length` | *텍스트 리뷰의 길이 입니다.(단어 갯수)* |
| `review_score` | *1부터5까지 점수를 나타냅니다* |<br><br>


![datacap](https://user-images.githubusercontent.com/79899868/235663380-ccfee586-4cd2-46c6-ba7d-e4c12e3c5759.png)<br>
<br>

ㄴ




