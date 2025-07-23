<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      For a guide and recipes on how to configure / customize this project,<br />
      check out the
      <a href="https://vuejs.org" target="_blank" rel="noopener"
        >Vue 3 documentation</a
      >.
    </p>
    <h3>Essential Vue 3 Features</h3>
    <ul>
      <li>
        <a
          href="https://vuejs.org/guide/essentials/reactivity-fundamentals.html"
          target="_blank"
          rel="noopener"
        >
          Composition API
        </a>
      </li>
      <li>
        <a
          href="https://vuejs.org/guide/typescript/overview.html"
          target="_blank"
          rel="noopener"
        >
          TypeScript Support
        </a>
      </li>
      <li>
        <a href="https://vitejs.dev" target="_blank" rel="noopener">
          Vite Build Tool
        </a>
      </li>
      <li>
        <a href="https://primevue.org" target="_blank" rel="noopener">
          PrimeVue Components
        </a>
      </li>
      <li>
        <a href="https://vitest.dev" target="_blank" rel="noopener">
          Vitest Testing
        </a>
      </li>
    </ul>
    <h3>Essential Links</h3>
    <ul>
      <li>
        <a href="https://vuejs.org" target="_blank" rel="noopener">Core Docs</a>
      </li>
      <li>
        <a href="https://discord.com/invite/vue" target="_blank" rel="noopener"
          >Community Chat</a
        >
      </li>
      <li>
        <a href="https://twitter.com/vuejs" target="_blank" rel="noopener"
          >Twitter</a
        >
      </li>
      <li>
        <a href="https://news.vuejs.org" target="_blank" rel="noopener">News</a>
      </li>
    </ul>
    <h3>Ecosystem</h3>
    <ul>
      <li>
        <a href="https://router.vuejs.org" target="_blank" rel="noopener"
          >vue-router</a
        >
      </li>
      <li>
        <a href="https://pinia.vuejs.org" target="_blank" rel="noopener"
          >pinia</a
        >
      </li>
      <li>
        <a
          href="https://github.com/vuejs/devtools#vue-devtools"
          target="_blank"
          rel="noopener"
        >
          vue-devtools
        </a>
      </li>
      <li>
        <a
          href="https://github.com/vuejs/awesome-vue"
          target="_blank"
          rel="noopener"
          >awesome-vue</a
        >
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
interface Props {
  msg: string
}

defineProps<Props>()
</script>

<style scoped>
.hello {
  margin: var(--spacing-xl) 0;
}

.hello h3 {
  margin: var(--spacing-xl) 0 var(--spacing-md);
}

.hello ul {
  list-style-type: none;
  padding: 0;
}

.hello li {
  display: inline-block;
  margin: 0 var(--spacing-sm);
}

.hello a {
  color: var(--color-primary);
}
</style>

