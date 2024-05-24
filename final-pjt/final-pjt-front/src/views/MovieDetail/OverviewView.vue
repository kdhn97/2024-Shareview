<template>
  <div class="overview-area">
    <p>{{ movie.overview }}</p>
  </div>
</template>

<script setup>
defineProps({
  movie: Object,
})
</script>

<style scoped>
.overview-area {
  position: relative;
  left: 6%;
  text-align: center;
  width: 88%;
  line-height: 150%;
  font-size: 120%;
}
</style>