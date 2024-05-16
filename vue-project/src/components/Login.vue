<template>
  <p @click="LoginVue" style="color: white;">로그인</p>
  <div class="login-popup" :class="isLogin">
    <div class="login-popup-detail">
      <div class="login-popup-title">
        <h1 style="color: #166AE8;">다각화</h1>
        <h3>로그인</h3>
      </div>
      <div class="input-txt-list">
        <p><input type="text" class="input-txt" placeholder="이메일"></p>
        <p><input type="text" class="input-txt" placeholder="비밀번호"></p>
        <button class="login-btn">로그인</button>
      </div>
      <div class="login-txt">
        <p style="color: #166AE8;">비밀번호를 잊어버리셨나요?</p>
        <p>계정이 없으신가요? 회원가입</p>
      </div>
      <button class="popup-close-btn" @click="LoginVueOff">x</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const isLogin = ref(null)

const LoginVue = function () {
  isLogin.value = 'display-show'
}
const LoginVueOff = function () {
  isLogin.value = ''
}
</script>

<style scoped>
.login-popup {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 400px;
  height: 500px;
  background-color: white;
  border: 1px solid black;
  border-radius: 3%;
  display: none;
}

.login-popup-detail {
  margin-top: 15%;
}

.login-popup-title,
.login-txt {
  text-align: center;
}

.input-txt-list {
  margin-top: 10%;
  position: relative;
  left: 21%;
}

.input-txt {
  padding: 3%;
  width: 50%;
}

.login-btn {
  position: relative;
  left: 15%;
  width: 20%;
  margin: 5%;
  padding: 2%;
  border-radius: 10%;
  border-style: none;
  background-color: #166AE8;
  color: white;
}

.popup-close-btn {
  position: absolute;
  left: 92%;
  top: 2%;
}

.display-show {
  display: block;
}
</style>