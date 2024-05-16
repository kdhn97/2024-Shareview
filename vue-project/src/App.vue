<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
      <nav>
        <RouterLink :to="{ name: 'home' }">Home</RouterLink> | 
        <RouterLink :to="{ name: 'choice' }">Choice</RouterLink>
      </nav>
  </header>

  <RouterView />
</template>

<style>
body {
  background-color: gray;
}
</style>
