import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
    path:'/register',
    name:'register',

    component: () => import('../views/RegisterView.vue')
    },
    {
      path:'/login',
      name:'login',

     component: () => import('../views/LoginView.vue')
    },
    {
    path:'/cars/new',
    name:'new-car',

    component: () => import('../views/CarFormView.vue')
   },
   {
    path:'/cars/:id',
    name:'car-details',

    component: () => import('../views/CarDetailsView.vue')
   },
    {
      path:'/logout',
      name:'logout',

      component: () => import('../views/LogoutView.vue')
    },
    {
      path:'/explore',
      name:'explore',

      component: () => import('../views/CarsView.vue')
    },
    {
      path:'/user/' + sessionStorage.getItem('user_id'),
      name:'user-details',

      component: () => import('../views/UserDetailsView.vue')
    }
  ]
})

export default router
