<template>
  <div class="profile-container">
    <!-- 비밀번호 변경 -->
    <form class="password-update" @submit.prevent="passwordUpdate">
      <h2>비밀번호 변경</h2>
      <label for="password1">새 비밀번호</label>
      <input type="text" name="password1" class="password" v-model="password1" placeholder="New Password">
      <label for="password2">새 비밀번호 확인</label>
      <input type="text" name="password2" class="password" v-model="password2" placeholder="Password Check">
      <input type="submit" class="password-btn" value="변경">
    </form>
  </div>

  <hr>

  <!-- 닉네임 변경하기 -->
  <form @submit.prevent="updateUsername" class="nickname">
    <h2>닉네임 변경</h2>
    <p>현재 닉네임</p>
    <p class="nownickname">{{ userData.nickname }}</p>
    <p>변경 닉네임</p>
    <input class="afternickname" type="text" placeholder="변경할 닉네임을 입력해주세요" v-model="newUsername" />
    <div>
      <input type="submit" class="nickname-btn" value="닉네임 변경">
    </div>
  </form>

  <hr>

  <!-- 회원탈퇴 -->
  <div class="profile-container">
    <p class="user-delete" @click="userDelete">회원정보 탈퇴</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useLoginStore } from '@/stores/login'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  profile: Object,
  userData: Object,
  loadUserData: Function,
})

// 닉네임 변경
const newUsername = ref('')
const updateUsername = () => {
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/api/v1/profile/change_nickname/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {
      nickname: newUsername.value
    }
  })
    .then((res) => {
      alert('닉네임 변경이 성공했습니다')
      newUsername.value = ''
      router.push({name: 'profile-like'})
      setInterval(function () { location.reload() }, 100)
    })
    .catch((err) => {
      console.log(err)
      alert("닉네임 변경에 실패했습니다.")
    })
}

const store = useLoginStore()
const router = useRouter()

const userDelete = function () {
  const flag = confirm('회원탈퇴를 하시겠습니까?')

  if (flag) {
    axios({
    method: 'delete',
    url: 'http://127.0.0.1:8000/api/v1/profile/member_leave/',
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      alert('회원 탈퇴가 실행되었습니다.')
      store.logout()
      router.push({ name: 'home' })
    })
    .catch(err => console.log(err))
  } else {
    alert('회원 가입이 취소되었습니다.')
  }

}


const password1 = ref('')
const password2 = ref('')

const passwordUpdate = function () {

  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/dj-rest-auth/password/change/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {
      new_password1: password1.value,
      new_password2: password2.value
    }
  })
    .then((res) => {
      alert('비밀번호 변경이 완료되었습니다')
      router.push({ name: 'profile-like' })
    })
    .catch(err => console.log(err))
}
</script>

<style scoped>
.nownickname {
  background-color: white;
  color: black;
  width: 12.3%;
  padding: 0.1% 0.5%;
  margin-left: 0.5%;
}

.afternickname {
  width: 12.3%;
  padding: 0.2% 0.4%;
  margin-left: 0.45%;
}

.nickname {
  color: white;
  position: relative;
  left: 3%;
}

.nickname-btn {
  margin: 1%  0%  0% 0.5%;
  width: 13.3%;
  border: 1px solid white;
  border-radius: 5px;
  background-color: black;
  color: white;
  padding: 0.2%;
}

.nickname-btn:hover {
  background-color: #166AE8;
  color: white;
  border-style: none;
}

.profile-container {
  position: relative;
  left: 3%;
  width: 95%;
  color: white;
}

hr {
  width: 95%;
  background: white;
  height: 1px;
  border: 0px;
  opacity: 0.5;
  margin-top: 1%;
}

.password-update {
  display: flex;
  width: 15%;
  flex-direction: column;
}

.password {
  margin: 3%;
  padding: 3%;
}

.user-delete {
  position: relative;
  left: 95%;
  font-size: 50%;
  text-align: center;
  width: 4%;
  border: 1px solid;
  padding: 0.2% 0%;
}

.user-delete:hover {
  background-color: red;
  border-style: none;
}

.password-btn {
  margin-left: 3%;
  width: 94%;
  border: 1px solid white;
  border-radius: 5px;
  background-color: black;
  color: white;
  margin-top: 3%;
  padding: 1%;
}

.password-btn:hover {
  background-color: #166AE8;
  color: white;
  border-style: none;
}
</style>