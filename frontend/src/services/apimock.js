import { credentials, passwords } from './mock/DB_Credentials.js'
import { logs } from './mock/DB_Logs.js'
import { UtilsMixins } from '@/helpers/Mixins'

var logged_user = {
    username: 'markzin',
    name: 'Mark Zuckerberg',
    email: 'zuck@facebook.com',
    notifications_enabled: true,
    permissions:{
        ADMIN: false,
        STAFF: false,
    }
};

function mockasync (data) {
    console.log(data)
    return new Promise((resolve) => {
        setTimeout(() => resolve({data: data}), 600)
    })
}

let loggedIn = true

const api = {
    login(username, password) {
        loggedIn = true
        return mockasync(logged_user)
    },
    logout() {
        loggedIn = false
        return mockasync({})
    },
    whoami() {
        const iam = {authenticated: loggedIn}
        if (iam.authenticated) {
            iam.user = logged_user
        }
        return mockasync(iam)
    },

    // Credentials
    getAllCredentials() {
        return mockasync(credentials).then(res => res.data)
    },
    getFavoriteCredentials() {
        return mockasync(credentials.filter(credential => credential.favorite)).then(res => res.data)
    },
    getCredentialByText(text) {
        return mockasync(credentials.filter(credential => {
			const searchText = credential.name + credential.username + credential.status + credential.link
			const normalizedText = UtilsMixins.methods.normalizeText(searchText)
			const normalizedSearch = UtilsMixins.methods.normalizeText(text)
			return normalizedText.includes(normalizedSearch)
		})).then(res => res.data)
    },
    getRecentAccessedCredentials(limit=5) {
        function _sortLastAccessed(a, b) {
            if (a.last_access > b.last_access) {
                return 1;
            }
            if (a.last_access < b.last_access) {
                return -1;
            }
            return 0
        }
        let orderedCredentials = credentials.sort(_sortLastAccessed).slice(0, limit)
        return mockasync(orderedCredentials).then(res => res.data)
    },
    getNumberOfCredentials() {
        return mockasync(credentials.length).then(res => res.data)
    },
    toggleCredentialFavorite(credentialId) {
        const credential = credentials.find(credential => credential.id === credentialId)
        return mockasync(!credential.favorite).then(res => res.data)
    },
    getCredentialPassword(credentialId) {
        const password = passwords.find(password => password.id === credentialId).password
        return mockasync(password).then(res => res.data)
    },
    deleteCredentialPassword(credentialId) {
        for (let index = 0; index < passwords.length; index++) {
            const credential = passwords[index]
            if (credential.id === credentialId) {
                passwords.splice(index, 1)
                break
            }
        }
        return mockasync({}).then(res => res.data)
    },
    saveCredential(credential) {
        const newCredential = {
            id: Math.ceil(Math.random() * 100),
            last_access: new Date(),
            last_update: new Date(),
            created_at: new Date(),
            ...credential
        }
        passwords.push(newCredential)
        return mockasync(newCredential).then(res => res.data)
    },

    // Logs
    getAllLogs() {
        return mockasync(logs).then(res => res.data)
    }
};

export default api;
