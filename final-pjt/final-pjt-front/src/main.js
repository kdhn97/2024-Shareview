import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { useLoginStore } from './stores/login'

import App from './App.vue'
import router from './router'

const app = createApp(App)
const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)
app.use(pinia)
app.use(router)

const store = useLoginStore()

router.beforeEach((to, from) => {
  if (!store.isLogin && to.name !== 'home'){
    alert('로그인이 필요합니다')
    return {name: 'home'}
  }
})

app.mount('#app')
