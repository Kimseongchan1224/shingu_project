# shingu_project
![review](https://user-images.githubusercontent.com/79899868/231330013-53ccb539-4bc6-4349-8a58-c418e07ff03e.png)

MobileBert를 이용하여 리뷰 긍부정을 예측해보는 프로젝트 입니다.

## 1.개요


### 1-1. 문제정의
우리 자주 사용하는 배달 앱을 사용 시 우리는 음식점을 고른다. 여기서 많은 사람들이 음식점 리뷰를 보고 구매의사를<br>
결정하는 경우가 많다. 사람들이 작성하는 리뷰를 알아서 긍정적인 반응과 부정적인 반응으로 분류하여 보기 편하게 만들고 <br>
싶은 마음이 생겼다.

### 1-2. 사회/사업 영향
최근 SNS와 온라인 커뮤니티의 발전으로 소비자들은 상품에 대한 평가를 평점과 직접 쓰는 텍스트 리뷰의 형태로 사람들과 공유를<br>
하여 합리적인 구매 결정을 위한 중요한 정보로 사용하고 있다. 또한 리뷰는 소비자의 구매의사결정뿐만 아니라 매출액에 큰 영향을 미친다.<br>
따라서 리뷰와 평점의 중요성이 점차 증가하고 있으며 기업에서는 이러한 정보를 마케팅에 적극적으로 활용하고 있다. 

### 1-3. 데이터
Kaggle에서 Restaurant Review 데이터를 사용하였습니다. @ARSH ANWAR(https://www.kaggle.com/datasets/d4rklucif3r/restaurant-reviews)

### 1-4. 데이터 가공 과정
![ing](https://user-images.githubusercontent.com/79899868/232393906-ee5e2b72-f81b-4846-821d-2599d7251d57.png)<br>

## 2.데이터

### 2-1. 구성
Kaggle에서 제공받은 Restaurant Review 데이터 ([Restaurant_Reviews.xlsx](https://github.com/Kimseongchan1224/shingu_project/files/11206689/Restaurant_Reviews.xlsx))<br><br>
이 데이터 세트에는 Reviews와 Liked라는 두 개의 행이 있다.<br>
Reviews 행은 소비자들이 남긴 텍스트 리뷰, Liked 행은 1과 0으로 입력이 되어있다.<br>
Liked 행에 1은 긍정적 리뷰가 입력되어 있고 0은 부정적인 리뷰가 입력되어 있다.

![TextReview](https://user-images.githubusercontent.com/79899868/231338041-a732fa52-fbc6-4ce0-be12-e429568aded4.png)<br>
### 2-2. 정보

![describe](https://user-images.githubusercontent.com/79899868/232367303-3e6037ab-e7f7-4ea7-9ee0-90b973972bc1.png)

데이터의 긍부정비율이 비슷한것을 볼 수 있다.<br>
![bar](https://user-images.githubusercontent.com/79899868/232367307-11329b9f-e185-4c2e-9b7f-478e647d0d17.png)<br>




