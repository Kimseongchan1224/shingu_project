# <div align=center>YouTube 댓글 긍부정 예측분석</div>

![you](https://user-images.githubusercontent.com/79899868/235564536-f334f776-56aa-494d-aaec-bba49b6d521c.png)<br>
<div align=center>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/></a>
<img src="https://img.shields.io/badge/PyTorch-E34F26?style=flat-square&logo=PyTorch&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=Jupyter&logoColor=white"/></a>
</div>

## 1. 개요

### 1-1. 문제정의
2021년도 기준으로 국내에서 4천319만 명의 사람이 유튜브(YouTube)를 사용한다고 집계되었다. 이는 한국 전체 인구 80%를 웃돈다. 한국인이 한 달간 가장 많이 쓴 앱 2위, 한국인이 한 달간 가장 오래 쓴 앱 1위로 유튜브가 선정되기도 하였다. 이러한 수치로 미루어 보았을 때 유튜브의 인기가 엄청나다는 것을 알 수 있다.<br>

유튜버에게 있어서 조회 수는 곧 수익으로 직결되므로 조회 수를 높이는 것은 유튜버에게 있어서 매우 중요하다. 높은 조회 수를 얻기 위해서 유튜버가 유튜브 동영상 시청자들의 니즈(needs)와 관심도(interest)를 파악하는 것은 필수적이다. 유튜브 시청자의 니즈와 관심도를 알아내기 위한 도구로 영상에 달린 댓글은 가장 좋은 수단이다. 유튜버는 유튜브 댓글을 통해 영상에 대한 반응을 확인하여 유튜브 이용자들의 관심도, 여론 등을 파악할 수 있다. 하지만 유튜버가 영상의 댓글들을 일일이 확인해 영상의 반응을 확인하는 것은 어려움이 따른다. 댓글 수가 적으면 괜찮겠지만, 댓글 수가 100개~200개 이상이 되면 이를 일일이 읽어보는 것은 한계가 있다. 이러한 불편함을 해소하기 위해 유튜브 영상의 댓글들을 분석해 긍정적인 댓글과 부정적인 댓글을 분류하기 위한 서비스를 만들어보았습니다. <br> 
>[출처:kpuce2022CD/TotheMoon](https://github.com/kpuce2022CD/TotheMoon)<br>

### 1-2. 유튜브 댓글의 영향

