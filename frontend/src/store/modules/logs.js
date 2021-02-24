import api from 'Apijs'

const state = () => ({
	logs: []
})

const mutations = {
	ADD_LOGS(state, logs) {
		logs.forEach(log => {
			const stateLog = state.logs.find(stateLog => stateLog.id === log.id)
			if (stateLog) {
				Object.keys(state.logs).forEach(key => {
					stateLog[key] = log[key]
				})
			}
			else {
				state.logs.push(log)
			}
		})
	}
}

const getters = {
	logs(state) {
		return state.logs
	}
}

const actions = {
	async getAllLogs({ commit, getters }) {
		const logs = await api.getAllLogs()
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