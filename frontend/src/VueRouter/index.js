import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../components/HomeView';
import AboutView from '../components/AboutView.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {name: 'nall1',  path: '/',  component: HomeView},
    {name: 'nall2', path: '/nall2', component: AboutView},
  ],
});

export default router;