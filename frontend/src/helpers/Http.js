import axios from 'axios'

const http = axios.create({
	baseUrl: process.env.BASE_URL
})

async function _get(url, params){
	return (await http.get(url, {params: params})).data
}

async function _post(url, params){
	var fd = new FormData();
	params = params || {}
	Object.keys(params).map((k) => {
			fd.append(k, params[k]);
	})
	return (await http.post(url, fd)).data
}

http.defaults.xsrfHeaderName = "X-CSRFToken";
http.defaults.xsrfCookieName = "csrftoken";


export const post = _post
export const get = _get