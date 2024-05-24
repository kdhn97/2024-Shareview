<template>
  <!-- 회원가입 버튼 -->
  <p @click="SignVueOn" class="sign" v-show="!store.isLogin">회원가입</p>
  <!-- 회원가입 팝업 -->
  <div class="sign-popup" :class="isSign">
    <div class="sign-popup-detail">
      <!-- 로고 및 제목 -->
      <div class="logo-title">
        <img src="../../public/Logo_img.png" alt="Logo" class="logo">
        <h1 style="color: #166AE8;">다각화</h1>
      </div>
      <!-- 회원가입 컨텐츠 -->
      <div class="sign-popup-content">
        <h3 style="text-align: center">회원가입</h3>
        <form @submit.prevent="signUpRequest">
          <!-- 닉네임 입력창 -->
          <p><input type="text" class="input-txt" placeholder="닉네임" maxlength="15" v-model="nickname"></p>
          <!-- 이름 입력창 -->
          <p><input type="text" class="input-txt" placeholder="이름" v-model="username"></p>
          <!-- 이메일 입력창 -->
          <p><input type="email" class="input-txt" placeholder="이메일" v-model="email"></p>
          <!-- 비밀번호 입력창 -->
          <p><input type="password" class="input-txt" placeholder="비밀번호" v-model="password1"></p>
          <!-- 비밀번호 확인 입력창 -->
          <p><input type="password" class="input-txt" placeholder="비밀번호 확인" v-model="password2"></p>
          <!-- 회원가입 버튼 -->
          <button class="sign-btn">회원가입</button>
        </form>
        <!-- 로그인 링크 -->
        <div class="sign-txt">
          <p>이미 가입하셨나요?</p>
          <p @click="SignupConvertLogin" style="color: #166AE8; text-decoration:underline; cursor: pointer;">로그인</p>
        </div>
      </div>
      <!-- 팝업 닫기 버튼 -->
      <button class="popup-close-btn" @click="SignVueOff">x</button>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useLoginStore } from '@/stores/login'
import axios from 'axios'

const store = useLoginStore()

// 데이터 상태
const username = ref(null)
const email = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const isSign = ref(null)

// 회원가입 팝업 활성화 함수
const SignVueOn = function () {
  isSign.value = 'display-show'
  loginOntoOff()
}

// 회원가입 팝업 비활성화 함수
const SignVueOff = function () {
  isSign.value = ''
}

// 입력 폼 초기화 함수
const clearForm = function () {
  username.value = null
  email.value = null
  password1.value = null
  password2.value = null
  nickname.value = null
}

// 회원가입 요청 함수
const signUpRequest = function () {
  axios({
    method: 'post',
    url: 'http://127.0.0.1:8000/dj-rest-auth/registration/',
    data: {
      username: username.value,
      email: email.value,
      password1: password1.value,
      password2: password2.value,
      nickname: nickname.value
    }
  })
    .then((res) => {
      alert('회원가입에 성공하였습니다')
      SignVueOff()
      clearForm()
    })
    .catch((err) => {
      alert("회원가입에 실패하였습니다")
      console.log(err);
    })
}

const props = defineProps({
  loginOn: Boolean
})

const emit = defineEmits(['SignupConvertLogin', 'loginOntoOff'])

const SignupConvertLogin = function () {
  emit('SignupConvertLogin')
  SignVueOff()
}

const loginOntoOff = function () {
  emit('loginOntoOff')
}

watch(
  () => props.loginOn,
  (flag) => {
    if(flag) {
      SignVueOn()
      props.loginOn = false
    }
  }
)

</script>

<style scoped>
/* 회원가입 버튼 스타일 */
.sign {
  position: absolute;
  top: 0%;
  right: 4%;
  color: white;
  cursor: pointer;
}

/* 회원가입 팝업 스타일 */
.sign-popup {
  z-index: 9999;
  background: linear-gradient(#212121, #212121) padding-box,
    linear-gradient(330deg, #e81cff, #40c9ff) border-box;
  border: 3px solid transparent;
  color: white;
  position: fixed;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 350px;
  height: 500px;
  border-radius: 3%;
  display: none;
}

/* 회원가입 팝업 디테일 스타일 */
.sign-popup-detail {
  margin-top: 10%;
}

/* 로고 및 제목 스타일 */
.logo-title {
  display: flex;
  justify-content: center;
  transform: translate(0%, -20%);
}

/* 제목 스타일 */
.logo-title h1 {
  transform: translate(0%, -20%);
}

/* 로고 이미지 스타일 */
.logo {
  width: 20%;
  height: 20%;
}

/* 회원가입 컨텐츠 스타일 */
.sign-popup-content {
  text-align: center;
  transform: translate(0%, -12%);
}

/* 회원가입 링크 스타일 */
.sign-txt {
  display: flex;
  justify-content: center;
}

.sign-txt p {
  margin: 4% 2% 0% 0%;
}

.input-txt {
  padding: 2%;
  width: 50%;
}

/* 회원가입 버튼 스타일 */
.sign-btn {
  padding: 2% 20%;
  color: white;
  border-style: none;
  border-radius: 10px;
  background-color: #166AE8;
}

/* 팝업 닫기 버튼 스타일 */
.popup-close-btn {
  left: 92%;
  top: 2%;
  position: absolute;
  cursor: pointer;
  color: white;
  background-color: transparent;
  border: none;
  font-size: 17px;
}

/* 팝업 표시 스타일 */
.display-show {
  display: block;
}
</style>