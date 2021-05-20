import { createRouter, createWebHistory } from "vue-router"
import store from '@/store/index'

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import(/* webpackChunkName: "home" */ "../views/Home/Home.vue"),
    meta: { authenticationRequired: true },
    children: [
      {
				path: '',
				name: 'Overview',
        component: () => import(/* webpackChunkName: "overview" */ "../views/Home/Overview.vue")
      },
      {
				path: 'credentials',
				name: 'Credentials',
        component: () => import(/* webpackChunkName: "credentials" */ "../views/Home/Credentials.vue")
			},
			{
				path: 'logs',
				name: 'Logs',
        component: () => import(/* webpackChunkName: "logs" */ "../views/Home/Logs.vue")
			}
    ]
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import(/* webpackChunkName: "login" */ "../views/Login.vue"),
    meta: { authenticationRequired: false }
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
  next()
})

export default router
