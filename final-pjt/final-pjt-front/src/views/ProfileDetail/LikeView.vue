<template>
  <div>
    <div class="profile-container">
      <h2>좋아요</h2>
      <div class="like-container">
        <div v-for="movie in userData.like_movies" class="post">
          <img :src="movie.poster" alt="#" width="200px" @click="goToMovie(movie.movie_id)">
        </div>
      </div>
    </div>

    <hr>

    <div class="profile-container">
      <h2>리뷰</h2>
      <div class="review-container">
        <div v-for="movie in reviewList" class="post">
          <img :src="movie.poster" alt="#" width="200px" @click="goToMovieReview(movie.movie_id)">
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useLoginStore } from '@/stores/login'
import axios from 'axios'

const store = useLoginStore()
const router = useRouter()

const props = defineProps({
  userData: Object,
})

// 리뷰 쓴 영화 목록
const reviewList = computed(() => {
  if (!props.userData || !props.userData.review_movies) {
    return []
  }
  const seenTitles = new Set()
  return props.userData.review_movies.filter(movie => {
    const isDuplicate = seenTitles.has(movie.title)
    seenTitles.add(movie.title)
    return !isDuplicate
  })
})

// 영화 상세정보로 이동
const goToMovie = function (movie_id) {
  router.push({ name: "movieDetail", params: { movie_id: movie_id } })
}

const goToMovieReview = function (movie_id) {
  router.push({ name: "movie-review", params: { movie_id: movie_id } })
}
</script>

<style scoped>
.profile-container {
  position: relative;
  left: 3%;
  width: 95%;
  color: white;
}

.like-container {
  display: flex;
}

hr {
  width: 95%;
  background: white;
  height: 1px;
  border: 0px;
  opacity: 0.5;
  margin-top: 1%;
}

.post {
  display: flex;
  padding-left: 1%;
  cursor: pointer;
}

.review-container {
  display: flex;
}
</style>