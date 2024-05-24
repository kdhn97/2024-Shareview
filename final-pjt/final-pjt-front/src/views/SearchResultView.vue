<template>
  <div class="out-post">
    <div class="poster-container"  v-for="movie in searchResult" :key="movie.movie_id">
      <img class="poster" @click="newMovieDetail(movie)" :src="movie.poster" alt="#">
    </div>
  </div>
  <div v-if="searchResult.length == 0">
    <p class="no-result">검색 결과가 존재하지 않습니다.</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const props = defineProps({
  searchResult: Array
})

// 포스터 클릭 시, 영화 Detail 페이지로 이동하기
const newMovieDetail = function (movie) {
  console.log(movie)
  router.push({ name: 'movieDetail', params: { movie_id: movie.movie_id } })
}
</script>

<style scoped>
.out-post {
  position: absolute;
  top: 5%;
  left: 9%;
}
.poster-container {
  display: inline;
}
.poster {
  width: 250px;
  margin: 30px;
  border-radius: 10px;
  cursor: pointer;
}
.no-result{
  color: white;
  font-size: 200%;
  margin-left: 2%;
}
</style>