<template>
  <div class="navbar-content">
    <RouterLink :to="{ name: 'profile-like' }" class="navbar-link">나의 영화</RouterLink>
    <RouterLink :to="{ name: 'profile-update' }" class="navbar-link">회원정보수정</RouterLink>
  </div>
  <RouterView :userData="userData" />
</template>

<script setup>
import { onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

defineProps({
  userData: Object
})

onMounted(() => {
  if (route.path === `/profile`) {
    router.replace({ name: 'profile-like' })
  }
})
</script>

<style scoped>
.navbar-content {
  position: absolute;
  top: 10.5%;
  left: 69.5%;
  height: auto;
}
.navbar-link {
  width: 20vh;
  color: white;
  text-decoration: none;
  font-size: 150%;
  padding-left: 1%;
}
</style>