# 2024_Movie_PJT
영화 추천 사이트🎬

## 다각화
- 주제 : 다양한 각도에서 영화를 추천해드립니다.

### 컴포넌트 구성
- App : 네비게이션바, 템플릿
- HomeView : 홈 화면 출력. 영화 목록을 모두 출력할 것
    - MovieDetail : 상세정보 (제목, 설명, 포스터 큰화면, 유튜브 예고편)
    - MovieComment : 영화 댓글 확인, 작성
- ChoiceView : 영화 추천 선택 출력
    - ChoiceCountry : 나라 선택
    - ChoiceGenre : 장르 선택
    - ChoiceProducer : 영화 감독, 배우, 영화사 선택
    - ChoiceDetail : 최종적인 영화 추천 결과 출력
- SearchView : 영화 검색 결과 띄우는 컴포넌트
- CommunityView : 커뮤니티 기능
    - CommunityList : 커뮤니티 글 표시
    - CommunityCreate : 커뮤니티 글 생성
- Profile : 프로필 출력

### 일정
- 5.16(목) : Vue: 메인페이지 프레임 제작, Django : DB에 데이터 저장 및 필요한 api 제작(건네 줄 json 형식 등), 로그인, 로그아웃 제작
- 5.17(금) : Vue: 영화 상세페이지 제작, Django: 필요한 데이터 건네주기 (주말) : Django 마무리
- 5.20(월) : Vue: 영화 추천 페이지 제작
- 5.21(화) : Vue : 영화 추천 페이지,  유저 기능(프로필, 등) (영화, 배우, 받아오는게 끝나야 함)
- 5.22(수) : 자바스크립트 효과 추가 (애니메이션, 반응형 등)
- 5.23(목) : 자바스크립트 효과 추가 (애니메이션, 반응형 등) (ppt)
- 5.24(금) : (오전) ppt 제작, 발표 연습

### 개발 환경
- 개발 툴 - HTML , CSS , JavaScript
- 웹 프레임워크 - Django
- JavaScipt프레임워크 - Vue 3
- css프레임워크 - BootStrap, Vuetify
- 협업 관리 툴, 소스 관리 - Github
- 아이디어 공유 - Notion
- 디자인 공유 - Figma
- Axios을 이용한 REST API 연동
- 반응형 웹 디자인

### 사용할 API
- TMDB + 영화진흥위원회 + 유튜브

### 메모
1. 데이터 받아와서, DB 만들기
2. api 건네줄 때 어떤 형식으로 줘야할지
3. 메인, 서브 페이지 구성
4. 만들기
5. 만들고 나서 꾸미기
6. (추가적인 내용), 기능 더 추가하기, 애니메이션 같은 효과 넣기