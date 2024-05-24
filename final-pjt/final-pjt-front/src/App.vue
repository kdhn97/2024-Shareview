<template>
  <!-- 네비게이션 바 -->
  <div class="navbar">
    <!-- 네비게이션 바 배경 -->
    <div class="navbar-background"></div>
    <!-- 네비게이션 바 콘텐츠 -->
    <nav class="navbar-content">
      <!-- 사이트 로고 이미지 -->
      <img src="../public/Logo_img.png" alt="Logo" class="logo">
      <!-- 홈 링크 -->
      <RouterLink :to="{ name: 'home' }" class="nav">다각화</RouterLink>
      <!-- 검색 창 -->
      <input 
        @keyup.enter="searchRequest" 
        type="text" name="search" 
        class="search-nav" 
        placeholder=" ▷ 영화, 배우, 감독을 검색해보세요"
        v-model="searchData"
      >
      <!-- 프로필 링크 -->
      <RouterLink :to="{ name: 'profile' }" class="profile-nav" v-show="store.isLogin">프로필</RouterLink>
    </nav>
  </div>
    <!-- 로그인 및 회원가입 컴포넌트 -->
  <Login 
    @login-convert-signup="LoginConvertSignup"
    @sign-up-onto-off="signUpOntoOff"
    :signUpOn="signUpOn"
  />
  <Signup 
    @signup-convert-login="SignupConvertLogin" 
    @login-onto-off="loginOntoOff"
    :loginOn="loginOn"
    />
  <!-- 라우터 뷰 -->
  <RouterView 
    @select-event="selectDataPass"
    :selectData="selectData"
    :searchResult="searchResult"
  />
</template>

<script setup>
import { ref } from 'vue'
import { useLoginStore } from './stores/login'
import axios from 'axios'
import Login from './components/Login.vue'
import Signup from './components/Signup.vue'
import { setQuarter } from 'date-fns'
import router from './router'

const store = useLoginStore()

const selectData = ref({})

// choice를 한 정보를 choicedetail로 넘겨줌
const selectDataPass = function (data) {
  console.log(data.value)
  selectData.value = data.value
}

const searchData = ref('')
const searchResult = ref([])
const searchRequest = function (query_data) {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/search/',
    params: {
      query_params: searchData.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      searchData.value = ''
      searchResult.value = res.data
      router.push({name: 'searchResult', props: { searchResult: searchResult.value }})
    })
    .catch((err) => {
      console.log(err)
    })
}

const loginOn = ref(false)
const signUpOn = ref(false)

// 로그인을 회원가입 창으로 바꾸기
const LoginConvertSignup = function () {
  loginOn.value = true
}

// 회원가입을 로그인으로 바꾸기
const SignupConvertLogin = function () {
  signUpOn.value = true
}

const loginOntoOff = function() {
  loginOn.value = false
}

const signUpOntoOff = function () {
  signUpOn.value = false
}

</script>

<style>
* {
  font-family: "NEXONFootballGothicBA1", sans-serif;
  font-weight: 300;
  font-style: normal;
}

@font-face {
  font-family: 'NEXONFootballGothicBA1';
  src: url('https://gcore.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.1/NEXONFootballGothicBA1.woff') format('woff');
}

.search-nav {
  position: relative;
  left: 65%;
  width: 15%;
  height: 40%;
  border-style: none;
}

.profile-nav {
  position: absolute;
  top: 1.65vh;
  right: 10%;
  font-size: 104%;
  color: white;
  text-decoration: none;
}

/* 네비게이션 바 배경 */
.navbar-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
}

/* 네비게이션 바 콘텐츠 */
.navbar-content {
  height: 100%;
  display: flex;
  align-items: center;
  padding: 0 20px;
  /* 좌우 패딩 추가 */
}

/* 네비게이션 링크 */
.nav {
  color: white;
  text-decoration: none;
  margin-right: 20px;
  /* 링크 사이 간격 추가 */
}

/* 네비게이션 바 */
.navbar {
  width: 100%;
  height: 50px;
  position: relative;
  background-color: #111111;
  /* 배경 색상을 여기로 이동 */
}

/* 로고 이미지 */
.logo {
  width: 50px;
  height: 50px;
}

/* 전체 body */
body {
  margin: 0%;
  background-color: black;
}
</style>
