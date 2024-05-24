<template>
  <div style="display: flex;">
    <!-- 채팅창 전체를 감싸는 div -->
    <div class="chat-container" :style="{ backgroundColor: chatBackgroundColor, color: fontColor }" ref="chatContainer">
      <!-- 지금까지의 채팅이 들어가는 영역 -->
      <div class="chat-list">
        <!-- 채팅 -->
        <div v-for="chat in chatList" :key="chat.id" :class="{ 'my-chat': currentUser.id === chat.user.id }">
          <div class="chat-array">
            <p>유저 : {{ chat.user.nickname }}</p>
            <p>채팅 : {{ chat.content }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- 버튼을 클릭하여 채팅 창의 색을 변경하는 버튼 -->
    <div class="change-color">
      <button class="back-color" @click="changeChatBackgroundColor">배경색 변경</button>
      <button class="font-color" @click="changeChatFont">글자색 변경</button>
    </div>

    <!-- 채팅 입력구간 -->
    <div class="chat-position">
      <form @submit.prevent="chatSubmit" class="chat-input">
        <input class="chat-txt" type="text" placeholder="20 Max Chat" v-model="chatMessage" maxlength="20">
        <input type="submit" class="chat-btn" value="전송하기">
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUpdated } from 'vue'
import { useRoute } from 'vue-router'
import { useLoginStore } from '@/stores/login'
import axios from 'axios'

const store = useLoginStore()
const route = useRoute()

defineProps({
  movie: Object,
})

const chatList = ref([])

// 메시지 불러오기
const loadMessage = function () {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/${route.params.movie_id}/chat/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      chatList.value = res.data
      console.log(chatList.value)
    })
    .catch(err => console.log(err))
}

// 현재 입력창의 메시지와 쌍방향 연결
const chatMessage = ref('')

// 채팅을 DB에 보내서 저장
const chatSubmit = function () {
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/api/v1/${route.params.movie_id}/chat/`,
    data: {
      content: chatMessage.value,
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      loadMessage()
      chatMessage.value = ''
    })
    .catch(err => console.log(err))
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

// 스크롤을 맨 아래로 내리는 함수
const scrollToBottom = () => {
  if (chatContainer.value) {
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight
  }
}

const chatContainer = ref(null)

onMounted(() => {
  loadMessage()
  scrollToBottom()

  const observer = new MutationObserver(() => {
    scrollToBottom()
  })

  const config = { childList: true, subtree: true }

  if (chatContainer.value) {
    observer.observe(chatContainer.value, config)
  }
})

// 채팅이 갱신될 때마다 스크롤을 맨 아래로 내리는 함수 호출
onUpdated(() => {
  scrollToBottom()
})

// 채팅 창의 배경 색을 저장하는 변수
const chatBackgroundColor = ref('black')

// 채팅 창의 글씨 색을 저장하는 변수
const fontColor = ref('white')

// 랜덤한 색상 생성 함수
const generateRandomColor = () => {
  const letters = '0123456789ABCDEF'
  let color = '#'
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)]
  }
  return color
}

// 채팅 창의 배경색을 변경하는 함수
const changeChatBackgroundColor = () => {
  // 랜덤한 배경색으로 변경
  const randomColor = generateRandomColor()
  chatBackgroundColor.value = randomColor
}

const changeChatFont = () => {
  // 랜덤한 글자색으로 변경
  const rendomFont = generateRandomColor()
  fontColor.value = rendomFont
}
</script>

<style scoped>
.back-color, .font-color {
  background-color: black;
  color: white;
  border-style: none;
  border: 1px solid white;
  padding: 5% 0%;
  cursor: pointer;
}

.back-color:hover, .font-color:hover {
  background-color: #166AE8;
  color: white;
  border-style: none;
}

.change-color {
  width: 5%;
  display: flex;
  flex-direction: column;
  position: relative;
  gap: 5%;
  margin-left: 0.5%;
}
.chat-position {
  position: absolute;
  top: 1%;
}
.chat-container {
  margin-left: 15%;
  width: 70%;
  height: 27vh;
  border: 2px solid white;
  overflow: auto;
}

/* 상대방 채팅 크기 */
.chat-list {
  margin: 0.5%;
  width: 31%;
}

/* 내 채팅 */
.my-chat {
  position: relative;
  left: 220%;
  width: 100%;
}

.chat-array {
  padding: 0% 2%;
  margin: 2%;
  border: 1px solid white;
}

.chat-position {
  position: absolute;
  top: 101%;
  left: 14.9%;
  width: 80.4%;
}

.chat-input {
  display: flex;
}

.chat-txt {
  background-color: white;
  padding: 0.5%;
  width: 76.2%;
}

.chat-btn {
  cursor: pointer;
  padding: 0% 3%;
  font-size: 110%;
  font-weight: bold;
}
</style>
