<template>
  <div>
    <div v-if="isLoading" class="loading-screen">
      <div class="loaderBar">
        <h1>Loding</h1>
      </div>
    </div>

    <!-- 3초 후 Loding이 끝나면 실행되는 화면 -->
    <div v-else>
      <!-- 장르 선택 섹션 -->
      <div class="movie-select">
        <h2>[ 장르 선택 ]</h2>
        <div class="poster">
          <!-- 장르 목록 -->
          <div v-for="genre in currentGenres" :key="genre.genre_id">
            <p class="post-txt" @click="genreSelect(genre.genre)"
              :class="{ 'is-selected': selectedParams.genre === genre.genre }">{{ genre.genre }}</p>
          </div>
          <div @click="resetGenre" v-if="currentGenres.length === 0">
            <p class="post-txt">X</p>
          </div>
          <!-- 이전/다음 장르 화살표 -->
          <div v-if="filteredGenres.length > 7">
            <h1 class="arrow5" @click="showPrevGenre">
              <p>&lt;</p>
            </h1>
            <h1 class="arrow1" @click="showNextGenre">
              <p>&gt;</p>
            </h1>
          </div>
        </div>

        <!-- 국가 선택 섹션 -->
        <h2>[ 국가 선택 ]</h2>
        <div class="poster">
          <!-- 국가 목록 -->
          <div v-for="country in currentCountries" :key="country.country_id">
            <p class="post-txt" @click="countrySelect(country.country)"
              :class="{ 'is-selected': selectedParams.country === country.country }">{{ country.country }}</p>
          </div>
          <div @click="resetCountry" v-if="currentCountries.length === 0">
            <p class="post-txt">X</p>
          </div>
          <!-- 이전/다음 국가 화살표 -->
          <div v-if="filteredCountries.length > 7">
            <h1 class="arrow6" @click="showPrevCountry">
              <p>&lt;</p>
            </h1>
            <h1 class="arrow2" @click="showNextCountry">
              <p>&gt;</p>
            </h1>
          </div>
        </div>

        <!-- 배우 선택 섹션 -->
        <h2>[ 배우 선택 ]</h2>
        <div class="poster">
          <!-- 배우 목록 -->
          <div v-for="actor in currentActors" :key="actor.actor_id" class="actor-poster">
            <img :src="actor.profile_image ? actor.profile_image : '../public/default_img.jpg'" class="post-img" :alt="actor.actor"
              @click="actorSelect(actor)" :class="{ 'is-selected': selectedParams.actor === actor }">
            <p class="actor-name">{{ actor.actor }}</p>
          </div>
          <div v-if="currentActors.length === 0">
            <p @click="resetActor" class="post-txt">X</p>
          </div>
          <!-- 이전/다음 배우 화살표 -->
          <div v-if="filteredActors.length > 7">
            <h1 class="arrow7" @click="showPrevActor">
              <p>&lt;</p>
            </h1>
            <h1 class="arrow3" @click="showNextActor">
              <p>&gt;</p>
            </h1>
          </div>
        </div>

        <!-- 감독 선택 섹션 -->
        <h2>[ 감독 선택 ]</h2>
        <div class="poster">
          <!-- 감독 목록 -->
          <div v-for="producer in currentProducers" :key="producer.producer_id" class="producer-poster">
            <img :src="producer.profile_image ? producer.profile_image : '../public/default_img.'" class="post-img"
              :class="{ 'is-selected': selectedParams.producer === producer }" alt="#" @click="producerSelect(producer)">
            <p class="product-name">{{ producer.producer }}</p>
          </div>
          <div v-if="currentProducers.length === 0">
            <p @click="resetProducer" class="post-txt">X</p>
          </div>
          <!-- 이전/다음 감독 화살표 -->
          <div v-if="filteredProducers.length > 7">
            <h1 class="arrow8" @click="showPrevProducer">
              <p>&lt;</p>
            </h1>
            <h1 class="arrow4" @click="showNextProducer">
              <p>&gt;</p>
            </h1>
          </div>
        </div>

        <!-- 홈으로/최종 선택 버튼 -->
        <div class="btn">
          <h4 class="select-end-btn" @click="goToHome">홈으로</h4>
          <h4 class="select-end-btn" @click="goToDetail" :selectedParams="selectedParams">최종 선택</h4>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, computed, onMounted, watch } from 'vue'
import { useRouter, RouterLink } from 'vue-router'

const isLoading = ref(true);

onMounted(() => {
  setTimeout(() => {
    isLoading.value = false;
  }, 1500); // 1.5초 후에 로딩 상태를 false로 변경
});


const router = useRouter()

// 부모 컴포넌트로 emit
const emit = defineEmits(['selectEvent'])

// 최종 선택 클릭 시, 선택 결과 페이지로 이동하기
const goToDetail = () => {
  emit('selectEvent', selectedParams)
  router.push({ name: 'choice_detail', props: { selectedParams: selectedParams.value } })
}

// 홈으로 클릭 시, 메인 페이지로 이동하기
const goToHome = () => {
  router.push({ name: 'home' })
  window.scrollTo(0, 0) // 이동 시 가장 최상단 고정
}

// 영화 정보 관련 데이터
const genres = ref([])
const countries = ref([])
const actors = ref([])
const producers = ref([])
const movies = ref([])

// 영화 상세 정보 받아오기
onMounted(() => {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/choice/'
  })
    .then((res) => {
      genres.value = res.data.genres
      countries.value = res.data.countries
      actors.value = res.data.actors
      producers.value = res.data.producers
      movies.value = res.data.movies
    })
    .catch((err) => console.log(err))
})

// 관리하는 인덱스
const startIndexGenre = ref(0)
const endIndexGenre = computed(() => Math.min(startIndexGenre.value + 7, filteredGenres.value.length))
const startIndexCountry = ref(0)
const endIndexCountry = computed(() => Math.min(startIndexCountry.value + 7, filteredCountries.value.length))
const startIndexActor = ref(0)
const endIndexActor = computed(() => Math.min(startIndexActor.value + 7, filteredActors.value.length))
const startIndexProducer = ref(0)
const endIndexProducer = computed(() => Math.min(startIndexProducer.value + 7, filteredProducers.value.length))

const currentGenres = computed(() => {
  return filteredGenres.value.slice(startIndexGenre.value, endIndexGenre.value)
})

const currentCountries = computed(() => {
  return filteredCountries.value.slice(startIndexCountry.value, endIndexCountry.value)
})

const currentActors = computed(() => {
  return filteredActors.value.slice(startIndexActor.value, endIndexActor.value)
})

const currentProducers = computed(() => {
  return filteredProducers.value.slice(startIndexProducer.value, endIndexProducer.value)
})

const showNextGenre = () => {
  if (endIndexGenre.value < filteredGenres.value.length) {
    startIndexGenre.value = Math.min(startIndexGenre.value + 1, filteredGenres.value.length - 7)
  }
}

const showNextCountry = () => {
  if (endIndexCountry.value < filteredCountries.value.length) {
    startIndexCountry.value = Math.min(startIndexCountry.value + 1, filteredCountries.value.length - 7)
  }
}

const showNextActor = () => {
  if (endIndexActor.value < filteredActors.value.length) {
    startIndexActor.value = Math.min(startIndexActor.value + 1, filteredActors.value.length - 7)
  }
}

const showNextProducer = () => {
  if (endIndexProducer.value < filteredProducers.value.length) {
    startIndexProducer.value = Math.min(startIndexProducer.value + 1, filteredProducers.value.length - 7)
  }
}

const showPrevGenre = () => {
  if (startIndexGenre.value > 0) {
    startIndexGenre.value = Math.max(startIndexGenre.value - 1, 0)
  }
}

const showPrevCountry = () => {
  if (startIndexCountry.value > 0) {
    startIndexCountry.value = Math.max(startIndexCountry.value - 1, 0)
  }
}

const showPrevActor = () => {
  if (startIndexActor.value > 0) {
    startIndexActor.value = Math.max(startIndexActor.value - 1, 0)
  }
}

const showPrevProducer = () => {
  if (startIndexProducer.value > 0) {
    startIndexProducer.value = Math.max(startIndexProducer.value - 1, 0)
  }
}

// 어떤 장르, 국가, 배우, 감독을 선택헀는지 저장할 변수
const selectedParams = ref({
  genre: null,
  country: null,
  actor: null,
  producer: null
})

const genreSelect = function (genre) {
  if (selectedParams.value.genre === genre) {
    selectedParams.value.genre = null
  } else {
    selectedParams.value.genre = genre
  }
}

const countrySelect = function (country) {
  if (selectedParams.value.country === country) {
    selectedParams.value.country = null
  } else {
    selectedParams.value.country = country
  }
}

const actorSelect = function (actor) {
  if (selectedParams.value.actor === actor) {
    selectedParams.value.actor = null
  } else {
    selectedParams.value.actor = actor
  }
}

const producerSelect = function (producer) {
  if (selectedParams.value.producer === producer) {
    selectedParams.value.producer = null
  } else {
    selectedParams.value.producer = producer
  }
}

const resetGenre = function () {
  selectedParams.value.genre = null
}

const resetCountry = function () {
  selectedParams.value.country = null
}

const resetActor = function () {
  selectedParams.value.actor = null
}

const resetProducer = function () {
  selectedParams.value.producer = null
}

// 현재 선택된 요소에 따라 영화를 필터링
const filteredMovies = computed(() => {
  return movies.value.filter(movie => {
    let isMatch = true

    if (selectedParams.value.genre) {
      // isMatch = isMatch && selectedParams.value.genre.includes(movie.genre)
      isMatch = isMatch && movie.genre.includes(selectedParams.value.genre)
    }
    if (selectedParams.value.country) {
      isMatch = isMatch && movie.country === selectedParams.value.country
    }
    if (selectedParams.value.actor) {
      // isMatch = isMatch && selectedParams.value.actor.includes(movie.actor)
      isMatch = isMatch && movie.actor.some(actor => actor.actor === selectedParams.value.actor.actor)
    }
    if (selectedParams.value.producer) {
      // isMatch = isMatch && selectedParams.value.producer.includes(movie.producer)
      isMatch = isMatch && movie.producer.some(producer => producer.producer === selectedParams.value.producer.producer)
    }

    return isMatch
  })
})

watch(selectedParams, () => {
  console.log('Filtered Movies:', filteredMovies.value)
  console.log(selectedParams.value)
}, { deep: true })


const filteredGenres = computed(() => {
  const usedGenres = new Set()
  filteredMovies.value.forEach(movie => {
    movie.genre.forEach(genre => {
      usedGenres.add(genre.id)
    })
  })
  // 선택된 장르 추가
  if (selectedParams.value.genre) {
    usedGenres.add(selectedParams.value.genre.id)
  }
  return genres.value.filter(genre => usedGenres.has(genre.id))
})

const filteredCountries = computed(() => {
  const usedCountries = new Set(filteredMovies.value.map(movie => movie.country))
  // 선택된 국가 추가
  if (selectedParams.value.country) {
    usedCountries.add(selectedParams.value.country.country)
  }
  return countries.value.filter(country => usedCountries.has(country.country))
})

const filteredActors = computed(() => {
  const usedActors = new Set()
  filteredMovies.value.forEach(movie => {
    movie.actor.forEach(actor => {
      usedActors.add(actor.actor)
    })
  })
  // 선택된 배우 추가
  if (selectedParams.value.actor) {
    usedActors.add(selectedParams.value.actor.actor)
  }
  return actors.value.filter(actor => usedActors.has(actor.actor))
})

const filteredProducers = computed(() => {
  const usedProducers = new Set()
  filteredMovies.value.forEach(movie => {
    movie.producer.forEach(producer => {
      usedProducers.add(producer.producer)
    })
  })
  // 선택된 프로듀서 추가
  if (selectedParams.value.producer) {
    usedProducers.add(selectedParams.value.producer.producer)
  }
  return producers.value.filter(producer => usedProducers.has(producer.producer))
})

watch(selectedParams, (newVal, oldVal) => {
  // This will trigger re-computation of filteredMovies, filteredCountries, filteredActors, and filteredProducers
  console.log('배우', filteredActors.value)
  console.log('감독', filteredProducers.value)
  console.log('장르', filteredGenres.value)
  console.log('나라', filteredCountries.value)
}, { deep: true })
</script>

<style scoped>

/* 3초동안 Loding 화면 */
.loaderBar {
  width: 30%;
  height: 10%;
  background: #cccccc;
  border-radius: 10px;
  position: absolute;
  top: 45%;
  left: 35%;
  overflow: hidden;
  z-index: -1;
}

.loaderBar h1 {
  text-align: center;
  color: white;
}

.loaderBar::before {
  content: "";
  position: absolute;
  height: 100%;
  animation: fillProgress 1.5s ease-in-out infinite, lightEffect 1s infinite linear;
  animation-fill-mode: forwards;
  z-index: -1;
}

@keyframes fillProgress {
  0% {
    width: 0;
  }

  50% {
    width: 50%;
  }

  100% {
    width: 100%;
  }
}

@keyframes lightEffect {

  0%,
  20%,
  40%,
  70%,
  80%,
  100% {
    background: linear-gradient(137deg, #ffdb3b 10%, #FE53BB 45%, #8F51EA 77%, #0044ff 87%);
  }
}

/* 슬라이더 화살표 스타일 */
.arrow1,
.arrow2,
.arrow5,
.arrow6 {
  position: absolute;
  font-size: 200%;
  width: 4%;
  opacity: 0.3;
  height: 10%;
  cursor: pointer;
}

.arrow3,
.arrow4,
.arrow7,
.arrow8 {
  position: absolute;
  font-size: 200%;
  width: 4%;
  height: 22%;
  opacity: 0.3;
  cursor: pointer;
}

.arrow1 p,
.arrow2 p,
.arrow5 p,
.arrow6 p {
  font-size: 150%;
  position: relative;
  top: -40%;
}

.arrow3 p,
.arrow4 p,
.arrow7 p,
.arrow8 p {
  font-size: 150%;
  position: relative;
  top: 8%;
}



/* 화살표에 호버 효과 적용 */
.arrow1:hover,
.arrow2:hover,
.arrow3:hover,
.arrow4:hover,
.arrow5:hover,
.arrow6:hover,
.arrow7:hover,
.arrow8:hover {
  opacity: 1;
}

/* 화살표 위치 및 스타일 조정 */
.arrow1,
.arrow2,
.arrow3,
.arrow4 {
  right: 0.5%;
}

.arrow5,
.arrow6,
.arrow7,
.arrow8 {
  left: -1.5%;
}

.arrow1,
.arrow5 {
  bottom: 82.5%;
}

.arrow2,
.arrow6 {
  bottom: 65.5%;
}

.arrow3,
.arrow7 {
  bottom: 37%;
}

.arrow4,
.arrow8 {
  bottom: 7%;
}


/* 영화 선택 영역 스타일 */
.movie-select {
  position: relative;
  left: 11%;
  width: 80%;
  color: white;
  text-align: center;
}

/* 포스터 그룹 스타일 */
.poster {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
}

/* 포스터 텍스트 스타일 */
.post-txt {
  margin: 0%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 175%;
  color: black;
  width: 180px;
  height: 90px;
  background-color: white;
  border-radius: 10px;
}

/* 포스터 이미지 스타일 */
.post-img {
  width: 180px;
  height: 210px;
  transition: opacity 0.3s, transform 0.3s;
  border-radius: 10px;
  cursor: pointer;
}

/* 포스터 텍스트 호버 효과 스타일 */
.post-txt:hover {
  font-weight: bold;
  color: white;
  background-color: darkgray;
  transform: scale(1.1);
}

/* 포스터 이미지 호버 효과 스타일 */
.post-img:hover {
  opacity: 0.5;
  transform: scale(1.1);
}

/* 배우/감독 이름 스타일 */
.actor-name,
.product-name {
  position: absolute;
  font-size: 150%;
  font-weight: bold;
  display: none;
  color: white;
}

.actor-name {
  top: 55%;
}

.product-name {
  top: 85%;
}

/* 배우 포스터 호버 시 이름 표시 */
.actor-poster:hover .actor-name {
  display: block;
}

/* 감독 포스터 호버 시 이름 표시 */
.producer-poster:hover .product-name {
  display: block;
}

/* 버튼 그룹 스타일 */
.btn {
  display: flex;
}

/* 선택 종료 버튼 스타일 */
.select-end-btn {
  margin: 1% 0% 1% 1%;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  left: 40.5%;
  width: 100px;
  height: 50px;
  border: 1px solid white;
  color: white;
}

/* 선택 종료 버튼 호버 효과 스타일 */
.select-end-btn:hover {
  color: white;
  border-style: none;
  background-color: #177AE8;
}

/* 선택된 이미지 */
.is-selected {
  border: rgb(235, 45, 45) 3px solid;
}
</style>