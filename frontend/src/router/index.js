import { createRouter, createWebHistory } from "vue-router"
import store from '@/store/index'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import(/* webpackChunkName: 'home' */ '../views/Home/Home.vue'),
    meta: { authenticationRequired: true },
    children: [
      {
				path: '',
				name: 'Overview',
        component: () => import(/* webpackChunkName: 'overview' */ '../views/Home/Overview.vue')
      },
      {
				path: 'credentials',
				name: 'Credentials',
        component: () => import(/* webpackChunkName: 'credentials' */ '../views/Home/Credentials.vue')
			},
			{
				path: 'logs',
				name: 'Logs',
        component: () => import(/* webpackChunkName: 'logs' */ '../views/Home/Logs.vue')
			}
    ]
  },
  {
    path: '/landing',
    name: 'Landing',
    component: () => import(/* webpackChunkName: 'landing' */ '../views/Landing/Landing.vue'),
    meta: { authenticationRequired: false },
    children: [
      {
        path: '',
        name: 'Login',
        component: () => import(/* webpackChunkName: "login" */ "../views/Landing/Login.vue")
      },
      {
        path: 'signup',
        name: 'Signup',
        component: () => import(/* webpackChunkName: "signup" */ "../views/Landing/Signup.vue")
      }
    ]
  },
  {
    path: '/:any(.*)',
    redirect: '/'
  }
];


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

router.beforeEach(async (to, from, next) => {
  if (to.meta.authenticationRequired && store.getters['auth/currentUser'] === undefined) {
    await store.dispatch('auth/whoami')
    if (!store.getters['auth/currentUser']) {
      next({ name: 'Login' })
    }
  }
  if (!to.meta.authenticationRequired && store.getters['auth/currentUser']) {
    next({ name: 'Overview' })
  }
  next()
})

export default router
