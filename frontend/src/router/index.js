import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import(/* webpackChunkName: "home" */ "../views/Home/Home.vue"),
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
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
