import { createApp } from "vue"
import App from "./App.vue"
import "./registerServiceWorker"
import router from "./router"
import store from "./store"
import Vuex from 'vuex'
import {eventBus, EVENTS} from './helpers/EventBus'

let app = createApp(App)

app.config.globalProperties.$eventBus = eventBus
app.config.globalProperties.$eventKeys = EVENTS

app
	.use(Vuex)
	.use(store)
	.use(router)
	.mount("#app")