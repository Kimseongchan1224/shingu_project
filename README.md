# YouTube 댓글 긍부정 예측분석
![yo](https://user-images.githubusercontent.com/79899868/234439912-dd1b0192-238b-4a73-b9ea-0f080bb224cb.png)
## 1. 개요
### 1-1. 문제정의
2021년도 기준으로 국내에서 4천319만 명의 사람이 유튜브(YouTube)를 사용한다고 집계되었다. 이는 한국 전체 인구 80%를 웃돈다. 한국인이 한 달간 가장 많이 쓴 앱 2위, 한국인이 한 달간 가장 오래 쓴 앱 1위로 유튜브가 선정되기도 하였다. 이러한 수치로 미루어 보았을 때 유튜브의 인기가 엄청나다는 것을 알 수 있다.<br>

최근에는 유튜브로 영상을 시청하는 사람뿐만 아니라 직접 유튜브에 영상을 업로드하여 수익을 창출하는 유튜버(Youtuber) 또한 증가하고 있는 추세이다. 아래 시각 자료는 수익을 창출하는 국내 유튜브 채널수를 그래프로 나타낸 것인데, 2019년에는 5만 6359만 개였는데 2020년에는 9만 7934만 개로 1년 새에 4만 1575개가 늘어났음을 알 수 있다. 또한 지난해 열린 ‘구글 포 코리아’행사에서 유튜브 최고 경영자(CEO) 수잔 워치 스키는 “지난해 유튜브는 한국 국내 총생산(GDP)에 약 1조 5천970억 원, 일자리 8만 6천30개를 창출하는 데 기여했다”라고 설명했다.<br>

유튜버에게 있어서 조회 수는 곧 수익으로 직결되므로 조회 수를 높이는 것은 유튜버에게 있어서 매우 중요하다. 높은 조회 수를 얻기 위해서 유튜버가 유튜브 동영상 시청자들의 니즈(needs)와 관심도(interest)를 파악하는 것은 필수적이다. 유튜브 시청자의 니즈와 관심도를 알아내기 위한 도구로 영상에 달린 댓글은 가장 좋은 수단이다. 유튜버는 유튜브 댓글을 통해 영상에 대한 반응을 확인하여 유튜브 이용자들의 관심도, 여론 등을 파악할 수 있다. 하지만 유튜버가 영상의 댓글들을 일일이 확인해 영상의 반응을 확인하는 것은 어려움이 따른다. 댓글 수가 적으면 괜찮겠지만, 댓글 수가 100개~200개 이상이 되면 이를 일일이 읽어보는 것은 한계가 있다. 이러한 불편함을 해소하기 위해 유튜브 영상의 댓글들을 분석해 긍정적인 댓글과 부정적인 댓글을 분류하기 위한 서비스를 만들어보았습니다. [출처:kpuce2022CD/TotheMoon](https://github.com/kpuce2022CD/TotheMoon)<br>
