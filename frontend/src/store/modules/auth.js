import api from 'Apijs'

const state = () => ({
    currentUser: null,
    token: undefined
})

const mutations = {
    SET_CURRENT_USER (state, user) {
        state.currentUser = user
    }
}

const getters = {
    currentUser (state) {
        return state.currentUser
    },
    loggedIn (state) {
        return !!(state.currentUser && state.currentUser.permissions)
    },
    token (state) {
        return state.token
    }
}

const actions = {
    async whoami ({ commit }) {
        const res = await api.whoami()
        if (res.data.authenticated) {
            commit('SET_CURRENT_USER', res.data.user)
        } else {
            commit('SET_CURRENT_USER', null)
        }
    }
}


export default {
	namespaced: true,
	state,
	mutations,
	getters,
	actions
}