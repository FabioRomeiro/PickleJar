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
        const res = await api.whoami()
        console.log(res)
        if (res.authenticated) {
            commit('SET_CURRENT_USER', res.user)
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