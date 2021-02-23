import { createApp } from "vue"
import App from "./App.vue"
import "./registerServiceWorker"
import router from "./router"
import store from "./store"
import Vuex from 'vuex'

createApp(App)
	.use(Vuex)
	.use(store)
	.use(router)
	.mount("#app")
