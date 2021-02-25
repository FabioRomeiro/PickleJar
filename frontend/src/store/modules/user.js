import api from 'Apijs'

const state = () => ({
	user: {
        username: 'markzin',
        name: 'Mark Zuckerberg',
        email: 'zuck@facebook.com',
        notifications_enabled: true,
        permissions:{
            ADMIN: false,
            STAFF: false,
        }
    }
})

const mutations = {
	LOGOUT(state) {
		
	}
}

const getters = {
	user(state) {
		return state.user
	}
}

const actions = {
	async logout({ commit, getters }) {
        await api.logout()
        commit('LOGOUT')
    }
}

export default {
	namespaced: true,
	state,
	mutations,
	getters,
	actions
}