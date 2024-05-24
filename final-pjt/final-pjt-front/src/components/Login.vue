<template>
  <div>
    <!-- 로그인 버튼 -->
    <p @click="LoginVueOn" v-show="!store.isLogin" class="login">로그인</p>
    <p @click="store.logout" v-show="store.isLogin" class="logout">로그아웃</p>
    <!-- 로그인 팝업 -->
    <div class="login-popup" :class="isLogin">
      <div class="login-popup-detail">
        <!-- 로고 및 제목 -->
        <div class="logo-title">
          <img src="../../public/Logo_img.png" alt="Logo" class="logo">
          <h1 style="color: #166AE8;">다각화</h1>
        </div>
        <!-- 로그인 컨텐츠 -->
        <div class="login-popup-content">
          <h3>로그인</h3>
          <form @submit.prevent="login">
            <!-- 아이디 입력창 -->
            <p><input type="text" class="input-txt" placeholder="아이디" v-model.trim="username"></p>
            <!-- 비밀번호 입력창 -->
            <p><input type="password" class="input-txt" placeholder="비밀번호" v-model.trim="password"></p>
            <!-- 로그인 버튼 -->
            <input class="login-btn" type="submit" value="로그인">
          </form>
          <!-- 회원가입 링크 -->
          <div class="sign-login">
            <p>계정이 없으신가요?</p>
            <p @click="LoginConvertSignup" style="color: #166AE8; text-decoration:underline; cursor: pointer;">회원가입</p>
          </div>
        </div>
        <!-- 팝업 닫기 버튼 -->
        <button class="popup-close-btn" @click="LoginVueOff">x</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useLoginStore } from '@/stores/login'
import { useRouter } from 'vue-router'

const props = defineProps({
  signUpOn: Boolean
})


const store = useLoginStore()
const router = useRouter()

const username = ref('')
const password = ref('')

// 로그인 함수
const login = function () {
  const payload = {
    username: username.value,
    password: password.value,
  }

  store.login(payload)
  if (store.loginResult === true) {
    // LoginVueOff()
    isLogin.value = ''
    username.value = ''
    password.value = ''
  } else {
    password.value = ''
  }
}

// 로그인 팝업 상태
const isLogin = ref(null)

// 로그인 팝업 활성화 함수
const LoginVueOn = function () {
  isLogin.value = 'display-show'
  signUpOntoOff()
}

// 로그인 팝업 비활성화 함수
const LoginVueOff = function () {
  isLogin.value = ''
}

// 로그인 끄고 회원가입 켜기

const emit = defineEmits(['LoginConvertSignup', 'signUpOntoOff'])

const LoginConvertSignup = function () {
  emit('LoginConvertSignup')
  LoginVueOff()
}

const signUpOntoOff = function () {
  emit('signUpOntoOff')
}

// 회원가입이 켜진다면 로그인 끄기
watch(
  () => props.signUpOn,
  (flag) => {
    if (flag) {
      LoginVueOn()
    }
  }
)
</script>

<style scoped>
/* 로그아웃 스타일 */
.logout {
  position: absolute;
  top: 0%;
  right: 4%;
  color: white;
  cursor: pointer;
}

/* 로그인 버튼 스타일 */
.login {
  position: absolute;
  top: 0%;
  right: 9%;
  color: white;
  cursor: pointer;
}

/* 로그인 팝업 스타일 */
.login-popup {
  background: linear-gradient(#212121, #212121) padding-box,
    linear-gradient(330deg, #e81cff, #40c9ff) border-box;
  border: 3px solid transparent;
  color: white;
  position: fixed;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 350px;
  height: 450px;
  border-radius: 3%;
  display: none;
  z-index: 9999;
}

/* 로그인 팝업 디테일 스타일 */
.login-popup-detail {
  margin-top: 15%;
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

/* 로그인 컨텐츠 스타일 */
.login-popup-content {
  text-align: center;
  transform: translate(0%, -10%);
}

/* 로그인 입력창 스타일 */
.input-txt {
  width: 50%;
  padding: 3%;
  margin: 1%;
}

/* 회원가입 링크 스타일 */
.sign-login {
  margin: 1%;
  display: flex;
  justify-content: center;
}

.sign-login p {
  padding: 1%
}

/* 로그인 버튼 스타일 */
.login-btn {
  margin-top: 1%;
  padding: 2% 23%;
  color: white;
  border-style: none;
  border-radius: 10px;
  background-color: #166AE8;
  cursor: pointer;
}

/* 팝업 닫기 버튼 스타일 */
.popup-close-btn {
  top: 2%;
  left: 92%;
  position: absolute;
  cursor: pointer;
  color: white;
  background-color: transparent;
  border: none;
  font-size: 17px;
}

/* 활성화된 팝업 표시 스타일 */
.display-show {
  display: block;
}
</style>
