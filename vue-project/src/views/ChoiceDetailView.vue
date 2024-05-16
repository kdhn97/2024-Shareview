<template>
  <div class="order">시간순</div>
  <div class="order">평점순</div>

  <div class="poster">
    <p class="post"></p>
    <p class="post"></p>
    <p class="post"></p>
    <p class="post"></p>
  </div>

  <div class="movie-content-list">
    <div class="movie-content">
      <p>제목 : 쇼생크 탈출</p>
      <p>방영일 : 24.05.10</p>
      <p>평점 : 5.0</p>
    </div>
    <div class="movie-content">
      <p>제목 : 쇼생크 탈출</p>
      <p>방영일 : 24.05.10</p>
      <p>평점 : 5.0</p>
    </div>
    <div class="movie-content">
      <p>제목 : 쇼생크 탈출</p>
      <p>방영일 : 24.05.10</p>
      <p>평점 : 5.0</p>
    </div>
    <div class="movie-content">
      <p>제목 : 쇼생크 탈출</p>
      <p>방영일 : 24.05.10</p>
      <p>평점 : 5.0</p>
    </div>
  </div>

  <div class="poster">
    <p class="post"></p>
    <p class="post"></p>
    <p class="post"></p>
    <p class="post"></p>
  </div>

  <div class="movie-content-list">
    <div class="movie-content">
      <p>제목 : 쇼생크 탈출</p>
      <p>방영일 : 24.05.10</p>
      <p>평점 : 5.0</p>
    </div>
    <div class="movie-content">
      <p>제목 : 쇼생크 탈출</p>
      <p>방영일 : 24.05.10</p>
      <p>평점 : 5.0</p>
    </div>
    <div class="movie-content">
      <p>제목 : 쇼생크 탈출</p>
      <p>방영일 : 24.05.10</p>
      <p>평점 : 5.0</p>
    </div>
    <div class="movie-content">
      <p>제목 : 쇼생크 탈출</p>
      <p>방영일 : 24.05.10</p>
      <p>평점 : 5.0</p>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
.order {
  display: inline-block;
  border: 1px solid black;
  margin: 3% 0% 1% 7%;
  padding: 0.5%;
}

.poster {
  display: flex;
  justify-content: space-evenly;
}

.post {
  width: 250px;
  height: 350px;
  background-color: black;
}

.movie-content-list {
  display: flex;
  justify-content: space-evenly;
}

.movie-content {
  text-align: center;
  width: 250px; 
  border: 1px solid black;
}
</style>