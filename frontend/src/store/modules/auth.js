import api from 'Apijs'

const state = () => ({
    currentUser: undefined
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
    }
}

const actions = {
    async whoami ({ commit }) {
        const data = await api.whoami()
        if (data.authenticated) {
            commit('SET_CURRENT_USER', data.user)
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