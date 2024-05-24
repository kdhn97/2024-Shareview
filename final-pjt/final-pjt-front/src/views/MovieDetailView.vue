<template>
  
  <div class="Figure">
    <div class="explan">
      <p>포스터</p>
      <p>좋아요</p>
    </div>
    <!-- 별 모양 (포스터 기능) -->
    <label for="">
      <div class="container" @click="toggleImg" ref="imgContainer">
        <input type="checkbox">
        <svg height="24px" id="Layer_1" version="1.2" viewBox="0 0 24 24" width="24px" xml:space="preserve"
          xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
          <g>
            <g>
              <path
                d="M9.362,9.158c0,0-3.16,0.35-5.268,0.584c-0.19,0.023-0.358,0.15-0.421,0.343s0,0.394,0.14,0.521    
                  c1.566,1.429,3.919,3.569,3.919,3.569c-0.002,0-0.646,3.113-1.074,5.19c-0.036,0.188,0.032,0.387,0.196,0.506    
                  c0.163,0.119,0.373,0.121,0.538,0.028c1.844-1.048,4.606-2.624,4.606-2.624s2.763,1.576,4.604,2.625    
                  c0.168,0.092,0.378,0.09,0.541-0.029c0.164-0.119,0.232-0.318,0.195-0.505c-0.428-2.078-1.071-5.191-1.071-5.191    
                  s2.353-2.14,3.919-3.566c0.14-0.131,0.202-0.332,0.14-0.524s-0.23-0.319-0.42-0.341c-2.108-0.236-5.269-0.586-5.269-0.586    
                  s-1.31-2.898-2.183-4.83c-0.082-0.173-0.254-0.294-0.456-0.294s-0.375,0.122-0.453,0.294C10.671,6.26,9.362,9.158,9.362,9.158z">
              </path>
            </g>
          </g>
        </svg>
      </div>
    </label>
  
    <!-- 하트 모양 (좋아요 기능) -->
    <label class="like-container">
      <input type="checkbox" @click="likeMovie" v-model="isLiked">
      <div class="like-checkmark">
        <svg viewBox="0 0 256 256">
          <rect fill="none" height="256" width="256"></rect>
          <path
            d="M224.6,51.9a59.5,59.5,0,0,0-43-19.9,60.5,60.5,0,0,0-44,17.6L128,59.1l-7.5-7.4C97.2,28.3,59.2,26.3,35.9,47.4a59.9,59.9,0,0,0-2.3,87l83.1,83.1a15.9,15.9,0,0,0,22.6,0l81-81C243.7,113.2,245.6,75.2,224.6,51.9Z"
            stroke-width="20px" stroke="#FFF" fill="none"></path>
        </svg>
      </div>
    </label>

  </div>

  <img class="show-img" :class="{ 'display-show': isImgVisible }" :src="backgroundImageSrc" alt="snapshot"
    ref="showImg" />

  <div>
    <h5 class="select-end-btn" @click="goToHome">Home</h5>

    <div class="background">
      <!-- 배경 이미지 -->
      <div class="background-filter">
        <img :src="backgroundImageSrc" alt="snapshot" />
        <!-- 그라데이션 오버레이 -->
        <div class="overlay"></div>
      </div>

      <!-- 내용 컨테이너 -->
      <div class="content-container">
        <!-- 영화 상세 정보 -->
        <article class="detail-container">
          <h1>{{ title }}</h1>
          <p>장르 : {{ genre.join(', ') }}</p>
          <p>국가 : {{ country }}</p>
          <p>개봉 상태 : {{ status }}</p>
          <p v-if="runningTime">러닝타임 : {{ runningTime }}분</p>
          <p v-if="openingDate">개봉 일자 : {{ openingDate }}</p>

        </article>
        <!-- 유튜브 플레이어 -->
        <div class="youtube-container">
          <iframe width="600" height="350" :src="videoUrl" frameborder="0"
            allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
          </iframe>
        </div>
      </div>

      <!-- 영화 선택 네비게이션 -->
      <div class="view-container">
        <MovieDetailNav :movie="movie" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useLoginStore } from '@/stores/login'
import axios from 'axios'
import MovieDetailNav from '@/components/MovieDetailNav.vue'

const router = useRouter()
const store = useLoginStore()

// 홈으로 클릭 시, 메인 페이지로 이동하기
const goToHome = () => {
  router.push({ name: 'home' })
  window.scrollTo(0, 0) // 이동 시 가장 최상단 고정
}

// 변수
const backgroundImageSrc = ref(null);
const title = ref('')
const overView = ref('');
const genre = ref([]);
const country = ref('');
const runningTime = ref('');
const status = ref('')
const openingDate = ref('')
const movie = ref('')
const route = useRoute();
const videoUrl = ref(null)
const isImgVisible = ref(false) // 이미지 표시 여부를 관리할 반응형 변수 추가

const imgContainer = ref(null);
const showImg = ref(null);

onMounted(() => {
  // 영화 정보 로드
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/movie/${route.params.movie_id}/`,
  })
    .then((res) => {
      movie.value = res.data
      backgroundImageSrc.value = res.data.snapshots[0].snapshot
      title.value = res.data.title
      overView.value = res.data.overview
      genre.value = res.data.genre
      country.value = res.data.country
      runningTime.value = res.data.running_time
      if (res.data.show_status == 0) {
        status.value = '개봉'
      } else if (res.data.show_status == 1) {
        status.value = '개봉 예정'
      } else {
        status.value = '기타'
      }
      if (res.data.opening_date) {
        openingDate.value = res.data.opening_date
      }
    })
    .catch(err => console.log(err))
    .then((res) => {
      // 유튜브 트레일러 로드
      const API_KEY = import.meta.env.VITE_YT_API_KEY

      axios({
        method: 'get',
        url: `https://www.googleapis.com/youtube/v3/search?key=${API_KEY}`,
        params: {
          part: 'snippet',
          q: `${title.value} 트레일러`,
          maxResults: 1,
          type: 'video',
        }
      })
        .then((res) => {
          videoUrl.value = `https://www.youtube.com/embed/${res.data.items[0].id.videoId}?autoplay=1&mute=1`
        })
        .catch(err => console.log(err))
    })

  // 전역 클릭 이벤트 리스너 추가
  window.addEventListener('click', hideImgOutsideClick);
})

onUnmounted(() => {
  // 전역 클릭 이벤트 리스너 제거
  window.removeEventListener('click', hideImgOutsideClick);
})

// 좋아요 여부를 저장할 반응형 변수
const isLiked = ref(false)

onMounted(() => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/${route.params.movie_id}/like/`,
    data: {
      movie_id: route.params.movie_id,
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      isLiked.value = res.data.is_liked
    })
    .catch(err => console.log(err))
})

// 영화 좋아요 기능
const likeMovie = function () {
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/api/v1/${route.params.movie_id}/like/`,
    data: {
      movie_id: route.params.movie_id,
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log(isLiked.value)
    })
    .catch(err => console.log(err))
}

// 이미지 표시 토글 기능
const toggleImg = function () {
  isImgVisible.value = !isImgVisible.value
}

// 전역 클릭 이벤트 리스너 함수
const hideImgOutsideClick = function (event) {
  if (!imgContainer.value.contains(event.target) && !showImg.value.contains(event.target)) {
    isImgVisible.value = false;
  }
}
</script>

<style scoped>
.Figure {
  position: relative;
  top: 5vh;
  left: 9.1vh;
}

.explan {
  display: flex;
  position: absolute;
  top: 4.5vh;
  left: 1vh;
  color: white;
  z-index: 1;
  gap: 22px;
  font-size: 75%
}

.show-img {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 50%;
  z-index: 1;
  display: none;
  border: 1px solid white;
}

.display-show {
  display: block;
}

.container input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

.container {
  display: block;
  cursor: pointer;
  user-select: none;
  position: absolute;
  color: white;
  z-index: 1;
  cursor: pointer;
}

.container svg {
  position: relative;
  top: 0;
  left: 0;
  height: 50px;
  width: 50px;
  transition: all 0.3s;
  fill: #ffeb49;
  animation: effect 400ms ease;
}

@keyframes effect {
  0% {
    transform: scale(0);
  }

  50% {
    transform: scale(1.2);
  }

  100% {
    transform: scale(1);
  }
}

.container svg:hover {
  transform: scale(1.1);
}

/* .container input:checked~svg {
  fill: #ffeb49;
} */


.like-container input {
  position: absolute;
  cursor: pointer;
  opacity: 0;
}

.like-container {
  position: absolute;
  top: 0.7vh;
  left: 3%;
  font-size: 20px;
  user-select: none;
  transition: 100ms;
  z-index: 1;
  cursor: pointer;
}

.like-checkmark {
  top: 0;
  left: 0;
  height: 2em;
  width: 2em;
  transition: 100ms;
  animation: dislike_effect 400ms ease;
}

.like-container input:checked~.like-checkmark path {
  fill: #FF5353;
  stroke-width: 0;
}

.like-container input:checked~.like-checkmark {
  animation: like_effect 400ms ease;
}

@keyframes like_effect {
  0% {
    transform: scale(0);
  }

  50% {
    transform: scale(1.2);
  }

  100% {
    transform: scale(1);
  }
}

@keyframes dislike_effect {
  0% {
    transform: scale(0);
  }

  50% {
    transform: scale(1.2);
  }

  100% {
    transform: scale(1);
  }
}

/* 배경 스냅샷 스타일 */
.background-filter {
  position: absolute;
  top: 5.5%;
  width: 100%;
  height: 90%;
}

.background-filter img {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* 그라데이션 오버레이 스타일 */
.overlay {
  position: absolute;
  width: 100%;
  height: 100%;
  background: linear-gradient(185deg, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 1) 65%), linear-gradient(270deg, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.7) 80%);
  pointer-events: none;
  /* 오버레이가 클릭 이벤트를 막지 않도록 */
}

/* 내용 컨테이너 스타일 */
.content-container {
  position: relative;
  top: 2vh;
  left: 1vh;
  display: flex;
  align-items: center;
}

/* 영화 상세 정보 컨테이너 스타일 */
.detail-container {
  color: white;
  padding-bottom: 2%;
  margin-left: 10%;
}

/* 영화 상세 정보 스타일 */
.detail-container>p {
  font-size: 25px;
}

.detail-container>h1 {
  font-size: 40px;
}

/* 유튜브 플레이어 컨테이너 스타일 */
.youtube-container {
  position: absolute;
  top: 12%;
  right: 10%;
}

/* 영화 선택 네비게이션 컨테이너 스타일 */
.view-container {
  top: 10%;
  color: white;
  position: relative;
}

/* 선택 종료 버튼 스타일 */
.select-end-btn {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  top: 4%;
  left: 1.5%;
  width: 3%;
  height: 3%;
  border: 1px solid white;
  color: white;
  z-index: 1;
}

/* 선택 종료 버튼 호버 효과 스타일 */
.select-end-btn:hover {
  color: white;
  border-style: none;
  background-color: #166AE8;
}
</style>