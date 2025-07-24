<template>
  <div id="app">
    <nav class="navbar">
      <div class="nav-brand">
        <h2>Flask Vue Starter</h2>
      </div>
      <ul class="nav-links">
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/vue-cli">Vue CLI</router-link></li>
        <li><router-link to="/about">About</router-link></li>
      </ul>
    </nav>
    <main class="main-content">
      <router-view />
    </main>
  </div>
</template>

<script setup lang="ts">
// No logic needed for basic navigation
</script>

<style>
#app {
  font-family: var(--font-family);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: var(--color-text);
  min-height: 100vh;
  background-color: var(--color-background);
}
</style>
