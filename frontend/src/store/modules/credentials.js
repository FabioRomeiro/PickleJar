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
            if (a.last_accessed > b.last_accessed) {
                return 1;
            }
            if (a.last_accessed < b.last_accessed) {
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
		const data = await api.getAllCredentials()
		commit('ADD_CREDENTIALS', data.credentials)
		return getters.credentials
	},
	async getFavoriteCredentials({ commit, getters }) {
		const data = await api.getFavoriteCredentials()
		commit('ADD_CREDENTIALS', data.credentials)
		return getters.favoriteCredentials
	},
	async getRecentAccessedCredentials({ commit, getters }, limit) {
		const data = await api.getRecentAccessedCredentials(limit)
		commit('ADD_CREDENTIALS', data.credentials)
		return getters.recentAccessedCredentials(limit)
	},
	async getCredentialByText({ commit, getters }, text) {
		const data = await api.getCredentialByText(text)
		commit('ADD_CREDENTIALS', data.credentials)
		return getters.credentials
	},
	async getNumberOfCredentials({ state, commit }) {
		const data = await api.getNumberOfCredentials()
		commit('SET_NUMBER_OF_CREDENTIALS', data.count_credentials)
		return state.numberOfCredentials
	},
	async toggleCredentialFavorite({ commit }, credential) {
		let newState = !credential.favorite
		try {
			await api.toggleCredentialFavorite(credential)
			commit('SET_CREDENTIAL_FAVORITE', {credential, favoriteState: newState})
		}
		catch(e) {
			console.log(e)
			newState = credential.favorite
		}
		return newState
	},
	async getCredentialPassword(context, credentialId) {
		const { password } = await api.getCredentialPassword(credentialId)
		return password
	},
	async deleteCredential({ state, commit }, credential) {
		await api.deleteCredentialPassword(credential.id)
		commit('REMOVE_CREDENTIAL', credential)
	},
	async saveCredential({ commit, getters }, credential) {
		const data = await api.saveCredential(credential)
		const updatedCredential = data.credential
		commit('ADD_CREDENTIALS', [updatedCredential])
		return getters.credentialById(updatedCredential.id)
	}
}

export default {
	namespaced: true,
	state,
	mutations,
	getters,
	actions
}