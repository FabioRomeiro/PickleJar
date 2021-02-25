import axios from 'axios'
import store from '@/store/index'

axios.defaults.headers.common.tabid = (Math.random() * 1e8).toFixed(0)

const http = axios.create({
	xsrfHeaderName: 'X-CSRFToken',
	xsrfCookieName: 'csrftoken',
	baseURL: process.env.API_BASE_URL,
	headers: {
		'Accept': 'application/json',
		'Content': 'application/json',
	}
})

http.interceptors.request.use(config => { 
	const token = store.getters['auth/token']
	if (token) {
		config.headers.Authorization = `Bearer ${token}`
	}

	return config 
}, Promise.reject)

let isHandlingExpiredToken = false
http.interceptors.response.use(response => response, error => {
	if (error.response && error.response.status !== 403) {
		return new Promise((resolve, reject) => {
			reject(error)
		})
  	}

	return new Promise((resolve, reject) => {
		isHandlingExpiredToken = false
		reject(error)
	})
})

export default http