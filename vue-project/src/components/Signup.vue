<template>
  <p @click="SignVue" style="color: white;">회원가입</p>
  <div class="sign-popup" :class="isSign">
    <div class="sign-popup-detail">
      <div class="sign-popup-title">
        <h1 style="color: #166AE8;">다각화</h1>
        <h3>회원가입</h3>
      </div>
      <div class="input-txt-list">
        <p><input type="text" class="input-txt" placeholder="이름"></p>
        <p><input type="text" class="input-txt" placeholder="이메일"></p>
        <p><input type="text" class="input-txt" placeholder="비밀번호"></p>
        <p><input type="text" class="input-txt" placeholder="비밀번호 확인"></p>
      </div>
      <button class="sign-btn">회원가입</button>
      <div class="sign-txt">
        <p style="color: #166AE8;">이미 가입하셨나요? 로그인</p>
      </div>
      <button class="popup-close-btn" @click="SignVueOff">x</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const isSign = ref(null)

const SignVue = function () {
  isSign.value = 'display-show'
}
const SignVueOff = function () {
  isSign.value = ''
}
</script>

<style scoped>
.sign-popup {
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

.sign-popup-detail {
  margin-top: 10%;
}

.sign-popup-title, .sign-txt {
  text-align: center;
}

.input-txt-list {
  position: relative;
  left: 21%;
}

.input-txt {
  padding: 3%;
  width: 50%;
}

.sign-btn {
  position: relative;
  left: 40%;
  width: 20%;
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