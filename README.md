# <div align=center>YouTube 댓글 긍부정 예측분석</div>

![you](https://user-images.githubusercontent.com/79899868/235564536-f334f776-56aa-494d-aaec-bba49b6d521c.png)<br>

<div align=center>YouTube는 구글이 운영하는 동영상 공유 서비스로, 사용자가 동영상을 업로드하고 시청하며 공유할 수 있도록 한다. <br> 당신(You)과 브라운관(Tube, 텔레비전)이라는 단어의 합성어이다.</div>
<div align=center>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/></a>
<img src="https://img.shields.io/badge/PyTorch-E34F26?style=flat-square&logo=PyTorch&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=Jupyter&logoColor=white"/></a>
</div><hr>

## 문제정의
- 유튜브의 규모가 커져가는 가운데 영상의 댓글을 알아서 분류해 주는 프로그램을 개발하고 싶었다.
- 댓글을 긍부정으로 분석하면 '크리에이터들이 영상을 구상하고 만드는데 좋은 피드백이 될 수 있지 않을까?'라는 생각이 들었다.
- 댓글을 알아서 분류해 주는 프로그램이 있으면 유튜브를 운영하는 크리에이터에게 큰 도움과 유튜브 측에서는 부정적인 댓글들 중 악성 댓글이 삭제가 된다면 올바른 인터넷 문화가 활성화가 될 것 같다.

## 댓글의 영향력
댓글의 영향력은 어느 정도일까? 사람들은 뉴스나 미디어를 통해 소식을 접할 때 댓글도 같이 읽는다는 응답이 90%나 되었다. 또한 단순히 주요 댓글만 읽지 않고 다른 댓글도 읽고 공감/비호감의 표시를 하는 등 적극적으로 댓글을 읽고 있었다. 댓글은 부정적인 측면과 긍정적인 측면이 있다. 한번 알아보자 <br>

부정적인 측면은 댓글의 여론 대표성과 댓글 내용 신뢰성에 부정적인 영향을 주고 있었다. 지만 자기주장이 강한 사람이 자극적인 내용의 댓글을 작성한다고 생각하며, 댓글 내용이나 주장은 믿을 만하지 못하다고 생각한다. 이러한 사실은 다수의 ‘공감’을 받은 베플에 대한 인식에서도 확인이 가능한데, 많은 ‘공감’으로 만들어진 베플의 내용이 다수의 의견과 일치하지 않는다는 의견이 다수였다.<br>

반면 긍정적인 측면은 댓글을 읽으며 공감이나 재미를 경험하고, 새로운 정보도 알게 되는 등 긍정적인 경험도 많이 한다. 사람들은 댓글의 부정적인 면과 긍정적인 면을 모두 인정하고 있으며, 따라서 댓글 자체를 없애는 것에는 반대하는 입장이다. 대신 댓글 실명제 도입, 댓글 내용 모니터링 강화, 명예훼손이나 허위사실 유포에 대한 처벌 강화 등 규제를 강화하는 데에는 찬성한다.<br>

댓글의 영향력, 더 나아가 포털사이트가 여론 형성에 미치는 영향력을 줄이는 정책에 대해서는 찬반 의견이 엇갈린다. 최근 제시되고 있는 여러 대안들 가운데 ‘공감수’ 정렬로 보이는 베플 기능을 없애야 한다는 주장과, 뉴스 아웃링크 정책을 도입해야 한다는 주장에 대해서는 모두 찬반 의견이 팽팽히 맞서는 결과가 나왔다. 의견 교환과 소통이라는 순기능을 그대로 유지하면서, 동시에 여론을 제대로 반영할 수 있는 최선의 방법이 무엇인지는 좀 더 고민이 필요한 것 같다.
>[출처:여론속의 여론 이동한 차장](https://hrcopinion.co.kr/archives/11809)<br>
## 예측분석 순서
![1](https://user-images.githubusercontent.com/79899868/235610290-be8fb94c-08a3-420e-acda-7803354810ea.png)<br>
- 분석할 유튜브 댓글 데이터 Kaggle에서 Excel 데이터 다운로드
- Excel 데이터를 pycham에서 인식할 수 있게 텍스트화 작업
- python을 활용하여 텍스트 데이터를 학습시키는 작업
- 학습이 된 프로그램을 작동시켜 긍정과 부정으로 분류하는지 확인
## 데이터 미리보기
[YouTube 댓글 데이터 @kaggle/ADVAY PATIL](https://www.kaggle.com/datasets/advaypatil/youtube-statistics/versions/1?resource=download)
| 데이터 | 구분 |
| --- | --- |
| `video ID` | *동영상 식별자입니다.* |
| `Comment` | *댓글 텍스트입니다.* |
| `Likes` | *댓글이 받은 좋아요 수입니다.* |
| `Sentiment` | *0의 값은 부정적 1 또는 2의 값은 각각 중립 및 긍정적인 감정을 나타냅니다.* |<br>
![datacap](https://user-images.githubusercontent.com/79899868/235628619-d250c769-0be8-45e9-8865-a280745407a1.png)


