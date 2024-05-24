<template>
  <div class="review-container">
    <div class="review-score-container">
      <!-- 총 평점 및 리뷰 작성 버튼 -->
      <p @click="showReviewModal" class="review-btn">리뷰 작성</p>
      <h1 class="total-score">총 평점 : {{ reviewAvg }}</h1>
      <!-- 리뷰 개수 -->
      <p class="total-score">{{ reviewNum }}개의 평점이 등록되었습니다</p>
    </div>
    <!-- 최신 순, 평점 순 버튼 -->
    <div class="sort-buttons">
      <p @click="orderByNew" class="btn">최신 순</p>
      <p @click="orderByScore" class="btn">평점 순</p>
    </div>
    <div class="review-list-container">
      <!-- 리뷰 목록 -->
      <div class="review-list">
        <div v-for="review in reviews" class="review-item">
          <div class="review-content">
            <p>{{ review.user.nickname }}</p>
            <p>{{ review.score }} 점</p>
            <p>{{ format(review.created_at, 'yyyy-MM-dd HH:mm:ss') }}</p>
            <p>{{ review.content }}</p>
          </div>
          <button v-show="isCurrentUser(review.user)" class="delete-button" @click="deleteReview(review.id)">✖</button>
        </div>
        <div v-if="reviews.length === 0" class="review-item">
          <div class="review-content">
            <p>아직 리뷰가 없습니다.</p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 리뷰 작성 모달 -->
  <MovieReviewForm v-if="reviewModalVisible" @closeModal="hideModal" />
</template>

<script setup>
defineProps({
  movie: Object,
})
import { onMounted, ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import { format } from 'date-fns'
import { useLoginStore } from '@/stores/login'
import axios from 'axios'
import MovieReviewForm from '@/components/MovieReviewForm.vue'

const route = useRoute()
const store = useLoginStore()

// 모달 관련 변수
const reviewModalVisible = ref(false)

// 모달 나타내기, 숨기기
const showReviewModal = function () {
  reviewModalVisible.value = true
}

const hideModal = function () {
  reviewModalVisible.value = false
}

// 리뷰 목록 가져오기
const reviews = ref([])

onMounted(() => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/${route.params.movie_id}/reviews/`
  })
    .then((res) => {
      reviews.value = res.data
    })
    .catch(err => {
      console.log(err)
    })
})

// 리뷰 관련 변수들
const reviewAvg = computed(() => {
  let reviewSum = 0
  if (reviews.value.length === 0) {
    return 0
  }
  reviews.value.forEach((review) => {
    reviewSum += review.score
  })
  return (reviewSum / reviews.value.length).toFixed(2)
})

const reviewNum = computed(() => {
  return reviews.value.length
})


// 리뷰 최신순 정렬
const orderByNew = function () {
  reviews.value.sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
}

// 리뷰 평점순 정렬
const orderByScore = function () {
  reviews.value.sort((a, b) => b.score - a.score)
}


// 리뷰 삭제 기능
const deleteReview = function (review_id) {
  axios({
    method: 'delete',
    url: `http://127.0.0.1:8000/api/v1/${route.params.movie_id}/reviews/`,
    data: {
      review_id
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      alert('리뷰가 정상적으로 삭제되었습니다.')
      location.reload(true)
    })
    .catch((err) => {
      alert('권한이 없습니다')
    })
}

// 현재 로그인된 유저 정보 가져오기
const currentUser = ref(null)
onMounted(() => {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/current_user/',
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      currentUser.value = res.data
    })
    .catch(err => console.log(err))
})

// 현재 유저가 리뷰 작성자인지 확인
const isCurrentUser = function (user) {
  return currentUser.value && user.id === currentUser.value.id
}
</script>

<style scoped>
.review-btn {
  border: 1px solid white;
  padding: 5px;
  width: 35%;
  text-align: center;
  cursor: pointer;
}

.btn {
  border: 1px solid white;
  padding: 5px;
  margin-left: 1%;
  cursor: pointer;
}

.btn:hover,
.review-btn:hover {
  background-color: #166AE8;
  border-style: none;
}

.review-container {
  display: flex;
  padding: 20px;
}

.review-score-container {
  position: relative;
  left: 12%;
}

.review-score-container p {
  margin-top: 3%;
  margin-left: 6%;
}

.review-list-container {
  position: absolute;
  top: 45%;
  left: 31.5%;
  width: 55%;
  overflow-y: auto;
  max-height: 25vh;
}

.total-score {
  display: flex;
  align-items: center;
  margin-left: 4%;
  width: 120%;
}

.sort-buttons {
  display: flex;
  position: absolute;
  top: 22%;
  left: 31%;
  width: 50%;
}

.sort-buttons button {
  margin-left: 1%;
}

.review-list {
  border: 1px solid #ccc;
  padding: 10px;
  background-color: #1f1f1f;
}

.review-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid #444;
  padding: 10px 0;
}

.review-item:first-child {
  border-top: none;
}

.review-content p {
  margin: 5px 0;
}

.delete-button {
  background-color: transparent;
  border: none;
  color: white;
  font-size: 20px;
  cursor: pointer;
  padding: 5px;
}

.delete-button:hover {
  color: red;
}
</style>