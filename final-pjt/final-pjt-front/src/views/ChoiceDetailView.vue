<template>
  <div class="out-post">
    <div v-for="movie in currentMovies">
      <div class="poster">
        <div>
          <img :src="movie.poster" alt="#" class="post" @click="newMovieDetail(movie)">
          <p>제목 : {{ movie.title }}</p>
        </div>
      </div>
    </div>

    <!-- 포스터 이전/다음 버튼 -->
    <div v-show="movies.length > 5">
      <div class="arrow arrow1" @click="showNextPoster1">
        <p> &lt; </p>
      </div>
      <div class="arrow arrow2" @click="showNextPoster2">
        <p> &gt; </p>
      </div>
    </div>

    <div v-show="movies.length === 0">
      <h1 style="color: white;">검색 결과가 없습니다</h1>
    </div>

    <p class="go-to-select" @click="goToSelect">돌아가기</p>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// 포스터 클릭 시, 영화 Detail 페이지로 이동하기
const newMovieDetail = function (movie) {
  router.push({ name: 'movieDetail', params: { movie_id: movie.movie_id } })
}

const props = defineProps({
  selectData: Object
})

// 돌아가기 클릭 시, 선택 페이지로 이동하기
const goToSelect = () => {
  router.push({ name: 'choice' })
}

// 필터링 된 영화 받아오기
const movies = ref([])

// 관리하는 인덱스
const startIndex = ref(0)
const endIndex = ref(5)

// 현재 영화 목록
const currentMovies = computed(() => {
  return movies.value.slice(startIndex.value, endIndex.value)
})

// 현재 포스터 표시
const showNextPoster1 = () => {
  if (startIndex.value !== 0) {
    startIndex.value -= 1
    endIndex.value -= 1
  }
}
const showNextPoster2 = () => {
  if (endIndex.value !== movies.value.length) {
    startIndex.value += 1
    endIndex.value += 1
  } else {
    startIndex.value = 0
    endIndex.value = 5
  }
}

const genre = props.selectData.genre ? props.selectData.genre : null
const country = props.selectData.country ? props.selectData.country : null
const actor_code = props.selectData.actor ? props.selectData.actor.actor_code : null
const producer = props.selectData.producer ? props.selectData.producer.producer_id : null

onMounted(() => {
  console.log(props.selectData)
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/choice/result/',
    params: {
      genre: genre,
      country: country,
      actor: actor_code,
      producer: producer,
    }
  })
    .then((res) => {
      movies.value = res.data
      console.log(movies.value)
    })
    .catch(err => console.log(err))
})

// 리뷰 목록 가져오기
const reviews = ref([])

// 리뷰 최신순 정렬
const orderByNew = function () {
  reviews.value.sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
}

// 리뷰 평점순 정렬
const orderByScore = function () {
  reviews.value.sort((a, b) => b.score - a.score)
}
</script>

<style scoped>
.arrow {
  position: absolute;
  font-size: 500%;
  width: 4%;
  height: 40%;
  color: white;
  cursor: pointer;
  opacity: 0.3;
}

.arrow:hover {
  opacity: 1;
}

.arrow1 {
  left: 1%;
  bottom: 30%;
}

.arrow2 {
  right: 0%;
  bottom: 30%;
}

.out-post {
  display: flex;
  justify-content: center;
  gap: 1%;
  margin-top: 7%;
}

.poster {
  text-align: center;
  color: white;
}

.post {
  width: 330px;
  height: 480px;
  z-index: 1;
  border-radius: 20px;
  cursor: pointer;
  padding: 3px;
  background-size: 200% 100%;
  background-image: linear-gradient(145deg, transparent 35%, #e81cff, #40c9ff);
  /* background-size를 추가 */
  background-position: 0% 50%;
  /* 초기 background-position을 설정 */
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

.post:hover {
  opacity: 0.75;
  transform: scale(1.05);
  /* 크기 커지는 애니메이션 */
}

.go-to-select {
  position: absolute;
  top: 80%;
  left: 47.5%;
  width: 5%;
  color: white;
  padding: 0.5% 0%;
  text-align: center;
  border: 1px solid white;
  cursor: pointer;
}
</style>
