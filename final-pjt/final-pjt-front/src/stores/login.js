import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useLoginStore = defineStore('login', () => {
  const token = ref(null)
  const router = useRouter()

  const loginResult = ref(null)

  const login = function (payload) {
    const username = payload.username
    const password = payload.password

    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/dj-rest-auth/login/',
      data: {
        username, password
      }
    })
      .then((res) => {
        token.value = res.data.key
        loginResult.value = true
        router.push({ name: 'home' })
        console.log(token.value)
        alert('로그인에 성공했습니다')
        setInterval(function () { location.reload() }, 100)
      })
      .catch(err => {
        console.log(err)
        alert('아이디와 비밀번호를 확인해주세요')
        loginResult.value = false
      })
  }

  const logout = function () {
    token.value = null
    alert('로그아웃 되었습니다.')
    router.push({name: 'home'})
  }

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  return { token, login, logout, isLogin, loginResult }
}, { persist: true })
