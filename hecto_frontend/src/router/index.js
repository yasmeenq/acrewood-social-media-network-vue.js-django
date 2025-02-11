import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SignupView from '@/views/SignupView.vue'
import LoginView from '@/views/LoginView.vue'
import FeedView from '@/views/FeedView.vue'
import MessagesView from '@/views/MessagesView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
        path: '/',
        name: 'home',
        component: HomeView

    },
    {
        path: '/signup',
        name: 'signup',
        component: SignupView

    },
    {
        path: '/login',
        name: 'login',
        component: LoginView

    },
    {
        path: '/feed',
        name: 'feed',
        component: FeedView

    },
    {
        path: '/messages',
        name: 'messages',
        component: MessagesView
    },
  ],
})

export default router
