import api from 'Apijs'

const state = () => ({
	logs: []
})

const mutations = {
	ADD_LOGS(state, logs) {
		state.logs = logs
	}
}

const getters = {
	logs(state) {
		return state.logs
	}
}

const actions = {
	async getAllLogs({ commit, getters }) {
		const { logs } = await api.getAllLogs()
		commit('ADD_LOGS', logs)
		return getters.logs
    }
}

export default {
	namespaced: true,
	state,
	mutations,
	getters,
	actions
}