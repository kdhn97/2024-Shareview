<template>
  <div>
    <!-- 메인 컨텐츠 -->
    <main>
      <!-- 배경 이미지 -->
      <img src="../../public/background_img.png" class="background-img" alt="background_img">

      <!-- 메인 텍스트 -->
      <div class="main-txt" :class="fadeMode">
        <div class="main-explan-txt">
          <h5>어떤 영화를 찾으시나요?</h5>
          <h1>당신을 위한 영화 추천 사이트</h1>
          <h5>다양한 시각에서 영화를 추천해드립니다</h5>
        </div>

        <!-- 추천 받기 버튼 -->
        <div class="recommend-btn" @click="recommend">
          <h2 class="recommend">추천 받기</h2>
        </div>

        <!-- 영화 정보 -->
        <div class="movie-info-cnt">
          <div class="movie-animation">
            <div class="movie-cnt">
              <h2>{{ movieCount }}</h2>
              <h2>{{ genreCount }}</h2>
              <h2>{{ producerCount }}</h2>
              <h2>{{ actorCount }}</h2>
              <h2>{{ countryCount }}</h2>
            </div>
            <div class="movie-cnt">
              <h2>영화 수</h2>
              <h2>장르 수</h2>
              <h2>감독 수</h2>
              <h2>배우 수</h2>
              <h2>국가 수</h2>
            </div>
          </div>
          <h3 class="scroll">Scroll ▽</h3>
        </div>
      </div>
    </main>

    <!-- 섹션 -->
    <section>
      <!-- 섹션 영화 -->
      <div class="section-movie">
        <h1>[ 현재 개봉작 ]</h1>
        <div class="movies-poster">
          <div class="posts" @click="newMovieDetail(movie)" v-for="movie in currentMovies1" :key="movie.movie_id">
            <img :src="movie.poster" class="poster" alt="#">
          </div>
          <!-- 포스터 이전/다음 버튼 -->
          <div class="arrow arrow1-1" @click="showNextPoster1_1">
            <p> &lt; </p>
          </div>
          <div class="arrow arrow1-2" @click="showNextPoster1_2">
            <p> &gt; </p>
          </div>
        </div>

        <h1>[ 개봉 예정작 ]</h1>
        <div class="movies-poster">
          <div class="posts" @click="newMovieDetail(movie)" v-for="movie in currentMovies2" :key="movie.movie_id">
            <img :src="movie.poster" class="poster" alt="#">
          </div>
          <!-- 포스터 이전/다음 버튼 -->
          <div class="arrow arrow2-1" @click="showNextPoster2_1">
            <p> &lt; </p>
          </div>
          <div class="arrow arrow2-2" @click="showNextPoster2_2">
            <p> &gt; </p>
          </div>
        </div>
      </div>

      <!-- SNS 로고 -->
      <div class="sns-logo">
        <a href="https://blog.naver.com/ehdgus3726"><img src="../../public/blog.png" alt="blog"></a>
        <a href="https://www.instagram.com/"><img src="../../public/instagram.png" alt="instagram"></a>
        <a href="https://www.youtube.com/"><img src="../../public/youtube.png" alt="youtube"></a>
      </div>

      <!-- 저작권 표시 -->
      <p class="copyright">Copyright ⓒ 2024. SSAFY All Right Reserved</p>

      <!-- 배경 모드 전환 버튼 - 로고 위에 덮어져있음 -->
      <h5 @click="modeOn" class='mode-btn'></h5>

      <!-- 영화 엔딩 크레딧 효과 -->
      <div class="credits" :class="ending_credit">
        <div class="left">
          <h2>팀장</h2>
          <h2>팀원</h2>
          <h2>기획</h2>
          <h2>알고리즘</h2>
          <h2>프론트엔드</h2>
          <h2>백엔드</h2>
          <h2>디자인</h2>
          <h2>ERD</h2>
          <h2>목업</h2>
          <h2>데이터</h2>
          <h2>컴포넌트</h2>
          <h2>API</h2>
          <h2>제작 지원</h2>
          <h2>장소 제공</h2>
          <h2>수고 많았습니다</h2>
        </div>
        <div class="right">
          <h2>김동현</h2>
          <h2>장효승</h2>
          <h2>김동현</h2>
          <h2>장효승</h2>
          <h2>김동현</h2>
          <h2>장효승</h2>
          <h2>김동현</h2>
          <h2>장효승</h2>
          <h2>김동현</h2>
          <h2>장효승</h2>
          <h2>김동현</h2>
          <h2>장효승</h2>
          <h2>SSAFY</h2>
          <h2>SSAFY</h2>
          <h2>부울경 1반♡</h2>
        </div>
      </div>

      <!-- 최상단으로 올라가는 버튼 -->
      <button @click="goTop" class="go-top-btn">
        <svg class="svgIcon" viewBox="0 0 384 512">
          <path
            d="M214.6 41.4c-12.5-12.5-32.8-12.5-45.3 0l-160 160c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L160 141.2V448c0 17.7 14.3 32 32 32s32-14.3 32-32V141.2L329.4 246.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3l-160-160z">
          </path>
        </svg>
      </button>
    </section>
  </div>
</template>

<!-- Vue 스크립트 -->
<script setup>
import axios from 'axios'
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useLoginStore } from '@/stores/login'
import Login from '@/components/Login.vue'
import Signup from '@/components/Signup.vue'

const router = useRouter()
const store = useLoginStore()

// 추천 받기 클릭 시, Choice 페이지로 이동
const recommend = function () {
  if (store.isLogin === true) {
    router.push({ name: 'choice' })
  } else {
    alert('로그인 후 사용 가능합니다.')
  }
}

// 포스터 클릭 시, 영화 Detail 페이지로 이동하기
const newMovieDetail = function (movie) {
  router.push({ name: 'movieDetail', params: { movie_id: movie.movie_id } })
}

// 영화 정보 개수
const movieCount = ref(0)
const genreCount = ref(0)
const producerCount = ref(0)
const actorCount = ref(0)
const countryCount = ref(0)
const currentMovieList = ref([])
const upcomingMovieList = ref([])

// 영화 정보 개수 받아오기
onMounted(() => {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/main/'
  })
    .then((res) => {
      movieCount.value = res.data.movie_count
      genreCount.value = res.data.genre_count
      producerCount.value = res.data.producer_count
      actorCount.value = res.data.actor_count
      countryCount.value = res.data.country_count
    })
    .catch(err => console.log(err))
})

//  영화 리스트 받아오기
onMounted(() => {
  // 현재 개봉 영화 리스트
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/current_movies/'
  })
    .then((res) => {
      currentMovieList.value = res.data
    })
    .catch(err => console.log(err))

  // 개봉 예정 영화 리스트
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/upcoming_movies/'
  })
    .then((res) => {
      upcomingMovieList.value = res.data
    })
    .catch(err => console.log(err))
})

// 관리하는 인덱스
const startIndex1 = ref(0)
const endIndex1 = ref(7)
const startIndex2 = ref(0)
const endIndex2 = ref(7)

// 현재 영화 목록
const currentMovies1 = computed(() => {
  return currentMovieList.value.slice(startIndex1.value, endIndex1.value)
})
const currentMovies2 = computed(() => {
  return upcomingMovieList.value.slice(startIndex2.value, endIndex2.value)
})

// 현재 포스터 표시
const showNextPoster1_1 = () => {
  if (startIndex1.value !== 0) {
    startIndex1.value -= 1
    endIndex1.value -= 1
  }
}
const showNextPoster1_2 = () => {
  if (endIndex1.value !== currentMovieList.value.length) {
    startIndex1.value += 1
    endIndex1.value += 1
  } else {
    startIndex1.value = 0
    endIndex1.value = 7
  }
}
// 다음 포스터 표시
const showNextPoster2_1 = () => {
  if (startIndex2.value !== 0) {
    startIndex2.value -= 1
    endIndex2.value -= 1
  }
}

const showNextPoster2_2 = () => {
  if (endIndex2.value !== upcomingMovieList.value.length) {
    startIndex2.value += 1
    endIndex2.value += 1
  } else {
    startIndex2.value = 0
    endIndex2.value = 7
  }
}

// 클릭 시, 모드 전환 활성화 (메인 화면만 보이게 되기)
const fadeMode = ref()

// 영화 엔딩 크레딧 효과
const ending_credit = ref()

const modeOn = function () {
  if (fadeMode.value === false || fadeMode.value === 'fade-out') {
    fadeMode.value = 'fade-in'
    ending_credit.value = 'credits-off'
  } else {
    fadeMode.value = 'fade-out'
    ending_credit.value = 'credits-on'
  }
}

// 최상단으로 올라가는 버튼
const goTop = function () {
  window.scrollTo({ left: 0, top: 0, behavior: 'smooth' })
}
// emit event
// 로그인 로그아웃 팝업을 띄우는 데 사용
const openSignup = function () {
  const isSignClicked = ref(true)
}
</script>

<!-- CSS 스타일 -->
<style scoped>
.credits {
  display: none;
}

.credits-on {
  display: block;
  position: absolute;
  left: 42%;
  width: 100%;
  text-align: center;
  animation: scrollUp 17s linear infinite;
  color: white;
}

@keyframes scrollUp {
  from {
    bottom: 0%;
  }

  to {
    bottom: 100%;
  }
}
.credits-off {
  display: none;
}

.left,
.right {
  position: absolute;
  flex: 1;
  text-align: center;
}

.left {
  text-align: right;
  padding-right: 10%;
}

.right {
  text-align: left;
  padding-left: 10%;
}

/* 모드 전환 버튼 */
.mode-btn {
  position: absolute;
  top: -1%;
  left: 1.7%;
  padding: 0.5%;
  z-index: 1;
  opacity: 0;
  cursor: pointer;
}

/* 페이드 인 애니메이션 */
.fade-in {
  opacity: 1;
  animation: fadeIn 2s forwards;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

/* 페이드 아웃 애니메이션 */
.fade-out {
  opacity: 1;
  animation: fadeOut 2s forwards;
}

@keyframes fadeOut {
  from {
    opacity: 1;
  }

  to {
    opacity: 0;
  }
}

/* 상단 화면 비율 */
main {
  width: 100%;
  height: 88vh;
}

/* 배경 이미지 */
.background-img {
  position: absolute;
  top: 0%;
  width: 100%;
  height: 100%;
  z-index: -1;
}

/* 메인화면 전체 텍스트 */
.main-txt {
  position: relative;
  top: 5%;
}

/* 메인화면 텍스트 */
.main-explan-txt {
  font-weight: bold;
  position: relative;
  text-align: center;
  font-size: 200%;
  color: white;
  /* 움직이는 애니메이션 */
  animation: moveLeft 2s;
}

/* 애니메이션 위치 영역 */
@keyframes moveLeft {
  0% {
    left: -100%;
  }

  100% {
    left: 0%;
  }
}

/* 추천 받기 버튼 */
.recommend {
  position: relative;
  left: 45%;
  padding: 1%;
  width: 8%;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  background-size: 300% 300%;
  transition: 0.5s;
  border: 1px solid;
  border-image: linear-gradient(137deg, #ffdb3b 10%, #FE53BB 45%, #8F51EA 67%, #0044ff 87%);
  border-image-slice: 1;
}

.recommend:hover {
  transform: scale(1.1);
  border-style: none;
  cursor: pointer;
  animation: gradient 10s ease infinite;
  background-image: linear-gradient(137deg, #ffdb3b 10%, #FE53BB 45%, #8F51EA 67%, #0044ff 87%);
}

.recommend-btn {
  position: relative;
  font-size: 120%;
  animation: moveRight 2s;
}

@keyframes moveRight {
  0% {
    right: -100%;
  }

  100% {
    right: 0%;
  }
}

/* 영화 정보 영역 */
.movie-info-cnt {
  position: relative;
  top: 5vh;
}

/* 영화 정보 갯수 */
.movie-cnt {
  display: flex;
  justify-content: space-evenly;
  color: white;
}

/* 움직이는 애니메이션 */
.movie-animation {
  position: relative;
  animation: moveUp 2s;
}

/* 애니메이션 위치 영역 */
@keyframes moveUp {
  0% {
    top: -100vh;
  }

  100% {
    top: 0;
  }
}

/* 스크롤 글자 */
.scroll {
  position: relative;
  text-align: center;
  color: white;
  margin-top: 3%;
  /* 움직이는 애니메이션 */
  animation: moveUpDown 2s infinite;
}

/* 애니메이션 위치 영역 */
@keyframes moveUpDown {
  0% {
    top: 0;
  }

  50% {
    top: 10px;
  }

  100% {
    top: 0;
  }
}

/* 하단 화면 비율 */
section {
  width: 100%;
  height: 90vh;
}

/* 상영 영화 목록 */
.section-movie {
  height: 90vh;
  position: relative;
  text-align: center;
  color: white;
}

/* 영화 포스터 위치 */
.movies-poster {
  display: flex;
  justify-content: space-evenly;
}

.posts {
  width: 24.5vh;
  height: 36.5vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  border-radius: 15px;
  background-size: 200% 100%;
  background-image: linear-gradient(145deg, transparent 35%, #e81cff, #40c9ff);
  animation: gradient 2.5s ease infinite;
}

@keyframes gradient {
  0% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }

  100% {
    background-position: 0% 50%;
  }
}

/* 영화 포스터 크기 */
.poster {
  border-radius: 15px;
  width: 24vh;
  height: 36vh;
  cursor: pointer;
}

.posts:hover {
  opacity: 0.75;
  /* 크기 커지는 애니메이션 */
  transform: scale(1.1);
}

/* 포스터 화살표 스타일 */
.arrow {
  position: absolute;
  font-size: 500%;
  width: 4%;
  height: 40%;
  color: white;
  cursor: pointer;
  opacity: 0.3;
}

.arrow1-1 p,
.arrow2-1 p {
  padding-top: 3vh;
  padding-right: 2vh;
}

.arrow1-2 p,
.arrow2-2 p {
  padding-top: 3vh;
  padding-left: 2vh;
}

.arrow1-1 {
  left: 0%;
  bottom: 53.5%;
}

.arrow1-2 {
  right: 0%;
  bottom: 53.5%;
}

.arrow2-1 {
  left: 0%;
  bottom: 4%;
}

.arrow2-2 {
  right: 0%;
  bottom: 4%;
}

.arrow:hover {
  opacity: 1;
}

/* SNS 로고 영역 */
.sns-logo {
  position: absolute;
  display: flex;
  height: 8vh;
  cursor: pointer;
}

/* SNS 로고 이미지 */
.sns-logo img {
  padding: 1vh 0vh 0vh 3vh;
  height: 4vh;
}

.sns-logo img:hover {
  transform: scale(1.2);
  /* 크기 커지는 애니메이션 */
}

/* 저작권 글자 */
.copyright {
  text-align: center;
  color: rgb(200, 200, 200);
}

/* 최상단으로 올라가는 버튼 */
.go-top-btn {
  bottom: 4%;
  right: -95%;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: rgb(20, 20, 20);
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0px 0px 0px 3px rgba(180, 160, 255, 0.253);
  cursor: pointer;
  transition-duration: 0.5s;
  overflow: hidden;
  position: relative;
}

.svgIcon {
  width: 12px;
  transition-duration: 0.5s;
}

.svgIcon path {
  fill: white;
}

.go-top-btn:hover {
  width: 75px;
  border-radius: 50px;
  transition-duration: 0.5s;
  background: linear-gradient(145deg, #e81cff, #40c9ff) border-box;
  align-items: center;
}

.go-top-btn:hover .svgIcon {
  transition-duration: 0.5s;
  transform: translateY(-200%);
}

.go-top-btn::before {
  position: absolute;
  bottom: -20px;
  content: "Go to Top";
  color: white;
  font-size: 0px;
}

.go-top-btn:hover::before {
  font-size: 13px;
  opacity: 1;
  bottom: unset;
  transition-duration: 0.5s;
}
</style>
