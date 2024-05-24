<template>
  <div>
    <div @click="newMovieDetail(movie)" v-for="movie in recommendedMovies" class="poster">
      <img :src="movie.poster" class="post" alt="#">
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()

defineProps({
  movie: Object,
})

// 포스터 클릭 시, 영화 Detail 페이지로 이동하기
const newMovieDetail = function (movie) {
  router.push({ name: 'movieDetail', params: { movie_id: movie.movie_id } })
  setInterval(function () { location.reload() }, 100)
}

const recommendedMovies = ref([])

onMounted(() => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/${route.params.movie_id}/associate/`,
  })
    .then((res) => {
      recommendedMovies.value = res.data
    })
    .catch(err => console.log(err))
})
</script>

<style scoped>
.poster {
  position: relative;
  left: 5%;
  display: inline;
}

.post {
  margin: 0.5% 1% 0% 0%;
  width: 270px;
  height: 270px;
  border-radius: 5%;
  cursor: pointer;
}
</style>