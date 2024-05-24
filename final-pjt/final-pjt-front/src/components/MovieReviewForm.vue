<template>
  <!-- 모달 전체 창 -->
  <div class="modal-overlay">
    <!-- 모달 내부 컨텐츠 -->
    <div class="modal-content">
      <button class="close-button" @click="closeModal">X</button>
      <h2>리뷰 작성</h2>

      <!-- 작성 form -->
      <form @submit.prevent="submitReview" class="form">
        <div class="score">
          <label for="score">평점 : </label>
          <input type="number" id="score" v-model="reviewScore" min="0" max="5" step="1" required>
        </div>
        <div class="review">
          <label for="review"></label>
          <textarea id="review" v-model="reviewContent" required placeholder="당신의 감상을 들려주세요."></textarea>
        </div>
        <button class="submit" type="submit">작성</button>
      </form>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useLoginStore } from '@/stores/login'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const store = useLoginStore()

const emit = defineEmits(['close'])

const closeModal = function () {
  emit('closeModal')
}

const reviewScore = ref(0)
const reviewContent = ref('')

// 리뷰 작성 요청
const submitReview = function () {
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/api/v1/${route.params.movie_id}/reviews/`,
    data: {
      score: reviewScore.value,
      content: reviewContent.value,
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      alert('리뷰 작성 완료')
      reviewScore.value = 0
      reviewContent.value = ''
      closeModal()
      location.reload(true)
    })
    .catch(err => {
      alert('리뷰 작성 권한이 없습니다')
    })
}
</script>

<style scoped>
.modal-overlay {
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(#212121, #212121) padding-box,
    linear-gradient(330deg, #e81cff, #40c9ff) border-box;
  border: 3px solid transparent;
  position: fixed;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 280px;
  height: 300px;
  border-radius: 3%;
}

.modal-content {
  color: white;
  padding: 20px;
  width: 300px;
  text-align: center;
  position: absolute;
  top: 0%;
}

.modal-content h2 {
  margin: 10% 0% 0% 0%;
}

.close-button {
  position: absolute;
  top: 5%;
  right: 10%;
  background: none;
  border: none;
  font-size: 20px;
  cursor: pointer;
  color: white;
}

.form {
  transform: translate(0%, 10%);
}

.score {
  margin: 5%;
}

.review {
  margin: 2%;
  padding: 2%;
}

#review {
  width: 200px;
  height: 50px;
}

.submit {
  margin: 2%;
  padding: 2% 8%;
  border-radius: 15%;
  font-weight: bold;
  font-size: 100%;
  cursor: pointer;
}

.submit:hover {
  background-color: #166AE8;
  border-style: none;
  color: white;
}
</style>