import api from 'Apijs'

const state = () => ({
	credentials: [],
	numberOfCredentials: 0
})

const mutations = {
	ADD_CREDENTIALS(state, credentials) {
		credentials.forEach(credential => {
			const stateCredential = state.credentials.find(stateCredential => stateCredential.id === credential.id)
			if (stateCredential) {
				Object.keys(state.credentials).forEach(key => {
					stateCredential[key] = credential[key]
				})
			}
			else {
				state.credentials.push(credential)
				state.numberOfCredentials += 1
			}
		})
	},
	SET_NUMBER_OF_CREDENTIALS(state, numberOfCredentials) {
		state.numberOfCredentials = numberOfCredentials
	},
	SET_CREDENTIAL_FAVORITE(state, {credential, favoriteState}) {
		const stateCredential = state.credentials.find(stateCredential => stateCredential === credential)
		stateCredential.favorite = favoriteState
	},
	REMOVE_CREDENTIAL(state, credential) {
		let index = state.credentials.indexOf(credential)
		state.credentials.splice(index, 1)
		state.numberOfCredentials -= 1
	},
	UPDATE_CREDENTIAL_FIELD(state, {credential, field, value}) {
		const index = state.credentials.indexOf(credential)
		state.credentials[index][field] = value
	}
}

const getters = {
	credentials(state) {
		return state.credentials
	},
	favoriteCredentials(state) {
		return state.credentials.filter(credential => credential.favorite)
	},
	recentAccessedCredentials(state) {
		function _sortLastAccessed(a, b) {
            if (a.last_access > b.last_access) {
                return 1;
            }
            if (a.last_access < b.last_access) {
                return -1;
            }
            return 0
        }
		return limit => state.credentials.sort(_sortLastAccessed).slice(0, limit)
	},
	numberOfCredentials(state) {
		return state.numberOfCredentials
	},
	credentialById(state) {
		return id => state.credentials.find(credential => credential.id === id)
	}
}

const actions = {
	async getAllCredentials({ commit, getters }) {
		const credentials = await api.getAllCredentials()
		commit('ADD_CREDENTIALS', credentials)
		return getters.credentials
    },
	async getFavoriteCredentials({ commit, getters }) {
		const credentials = await api.getFavoriteCredentials()
		commit('ADD_CREDENTIALS', credentials)
		return getters.favoriteCredentials
    },
    async getRecentAccessedCredentials({ state, commit, getters }, limit) {
		const credentials = await api.getRecentAccessedCredentials(limit)
		commit('ADD_CREDENTIALS', credentials)
		return getters.recentAccessedCredentials(limit)
    },
    async getNumberOfCredentials({ state, commit }) {
		const numberOfCredentials = await api.getNumberOfCredentials()
		commit('SET_NUMBER_OF_CREDENTIALS', numberOfCredentials)
		return state.numberOfCredentials
    },
    async toggleCredentialFavorite({ commit }, credential) {
		let newState = !credential.favorite
		commit('SET_CREDENTIAL_FAVORITE', {credential, favoriteState: newState})
		try {
			newState = await api.toggleCredentialFavorite(credential.id)
		}
		catch(e) {
			commit('SET_CREDENTIAL_FAVORITE', {credential, favoriteState: credential.favorite})
		}
		return newState
	},
	async getCredentialPassword(context, credentialId) {
		return await api.getCredentialPassword(credentialId)
	},
	async deleteCredential({ state, commit }, credential) {
		await api.deleteCredentialPassword(credential.id)
		commit('REMOVE_CREDENTIAL', credential)
	},
	async saveCredential({ commit, getters }, credential) {
		const newCredential = await api.saveCredential(credential)
		commit('ADD_CREDENTIALS', [newCredential])
		return getters.credentialById(newCredential.id)
	}
}

export default {
	namespaced: true,
	state,
	mutations,
	getters,
	actions
}