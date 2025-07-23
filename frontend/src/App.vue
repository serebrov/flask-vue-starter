<template>
  <div id="app">
    <Menubar :model="menuItems" class="mb-4">
      <template #start>
        <span class="font-bold text-xl">Flask Vue Starter</span>
      </template>
    </Menubar>
    <router-view />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const menuItems = ref([
  {
    label: 'Home',
    icon: 'pi pi-home',
    command: () => router.push('/')
  },
  {
    label: 'Vue CLI',
    icon: 'pi pi-cog',
    command: () => router.push('/vue-cli')
  },
  {
    label: 'About',
    icon: 'pi pi-info-circle',
    command: () => router.push('/about')
  }
])
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  min-height: 100vh;
  background-color: #f8f9fa;
}

.mb-4 {
  margin-bottom: 1rem;
}
</style>