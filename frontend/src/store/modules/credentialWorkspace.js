import api from 'Apijs'
import store from '../index'

const state = () => ({
    credential: null,
    password: undefined,
    editMode: false
})

const mutations = {
    CLOSE_WORKSPACE(state) {
        state.credential = null
        state.password = undefined
        state.editMode = false
    },
    OPEN_WORKSPACE(state, {credential, editMode}) {
        state.credential = credential
        state.editMode = editMode
    },
    SET_PASSWORD(state, password) {
        state.password = password
    },
    SET_CREDENTIAL_FIELD(state, {field, value}) {
        store.commit('credentials/UPDATE_CREDENTIAL_FIELD', {
            credential: state.credential,
            field,
            value
        })
    }
}

const getters = {
    editMode(state) {
        return state.editMode
    },
    credential(state) {
        return state.credential
    },
    password(state) {
        return state.password
    }
}

const actions = {
    
}

export default {
	namespaced: true,
	state,
	mutations,
	getters,
	actions
}