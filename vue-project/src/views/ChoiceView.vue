<template>
  <div class="movie-select">
    <h1>[ 장르 선택 ]</h1>
    <div class="poster">
      <p class="post"></p>
      <p class="post"></p>
      <p class="post"></p>
      <p class="post"></p>
      <p class="post"></p>
      <p class="post"></p>
    </div>
    <h1>[ 국가 선택 ]</h1>
    <div class="poster">
      <p class="post"></p>
      <p class="post"></p>
      <p class="post"></p>
      <p class="post"></p>
      <p class="post"></p>
      <p class="post"></p>
    </div>
    <h1>[ 배우 선택 ]</h1>
    <div class="poster">
      <p class="post2"></p>
      <p class="post2"></p>
      <p class="post2"></p>
      <p class="post2"></p>
      <p class="post2"></p>
      <p class="post2"></p>
    </div>
    <h1>[ 감독 선택 ]</h1>
    <div class="poster">
      <p class="post2"></p>
      <p class="post2"></p>
      <p class="post2"></p>
      <p class="post2"></p>
      <p class="post2"></p>
      <p class="post2"></p>
    </div>

    <p class="select-end-btn" @click="goToDetail">최종 선택</p>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goToDetail = function () {
  router.push({name: 'choice_detail'})
}
</script>

<style scoped>
.movie-select {
  text-align: center;
}

.poster {
  display: flex;
  justify-content: space-evenly;
}

.post {
  width: 150px;
  height: 100px;
  background-color: black;
}

.post2 {
  width: 150px;
  height: 200px;
  background-color: black;
}

.select-end-btn {
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  left: 46.5%;
  width: 100px;
  height: 50px;
  border: 1px solid black;
}

.select-end-btn:hover {
  background-color: #166AE8;
  border-style: none;
}
</style>