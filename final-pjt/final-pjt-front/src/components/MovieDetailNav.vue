<template>
  <!-- 영화 네비게이션 바 컨테이너 -->
  <div class="movie-navbar-container">
    <!-- 네비게이션 바 내용 -->
    <div class="navbar-content">
      <!-- 영화 소개 링크 -->
      <RouterLink :to="{ name: 'movie-overview' }" :movie="movie" class="navbar-link">소개</RouterLink>
      <!-- 리뷰 링크 -->
      <RouterLink :to="{ name: 'movie-review' }" class="navbar-link">리뷰</RouterLink>
      <!-- 추천 링크 -->
      <RouterLink :to="{ name: 'movie-recommend' }" class="navbar-link">추천</RouterLink>
      <!-- 채팅방 링크 -->
      <RouterLink :to="{ name: 'movie-chat' }" class="navbar-link">채팅방</RouterLink>
    </div>
  </div>
  <!-- 수평 구분선 -->
  <hr style="width: 95%;">
  <!-- 라우터 뷰 -->
  <RouterView :movie="movie" />
</template>

<script setup>
// Props 정의
defineProps({
  movie: Object,
})

import { onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

onMounted(() => {
  if (route.path === `/movie/${route.params.movie_id}`) {
    router.replace({name: 'movie-overview', params: {movie_id: route.params.movie_id}})
  }
})

</script>

<style scoped>
/* 영화 네비게이션 바 컨테이너 스타일 */
.movie-navbar-container {
  color: white;
  display: flex;
  justify-content: center;
}

/* 네비게이션 바 내용 스타일 */
.navbar-content {
  font-size: 30px;
  margin-bottom: 0.5%;
}

/* 네비게이션 링크 스타일 */
.navbar-link {
  position: relative;
  left: -85%;
  width: 16vh;
  text-decoration: none;
  color: white;
}

/* 네비게이션 링크 호버 스타일 */
.navbar-link:hover {
  transform: scale(1.2);
}
</style>