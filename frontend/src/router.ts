import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'
import VueCli from './views/VueCli.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/vue-cli',
      name: 'vue-cli',
      component: VueCli,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('./views/About.vue'),
    },
  ],
})

export default router
