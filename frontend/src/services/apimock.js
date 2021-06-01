import { credentials, passwords } from './mock/DB_Credentials'
import { logs } from './mock/DB_Logs'
import { image_url } from './mock/DB_PassImage'
import { UtilsMixins } from '@/helpers/Mixins'

var logged_user = {
    id: 1,
    first_name: 'Mark',
    last_name: 'Zuckerberg',
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
        setTimeout(() => resolve(data), 600)
    })
}

let loggedIn = true

const api = {
    login(username, password) {
        loggedIn = true
        return mockasync(logged_user)
    },
    signup(email, imageUrl, data) {
        return mockasync({})
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
        return mockasync({ credentials })
    },
    getFavoriteCredentials() {
        return mockasync({ credentials: credentials.filter(credential => credential.favorite) })
    },
    getCredentialByText(text) {
        return mockasync({ credentials: credentials.filter(credential => {
			const searchText = credential.name + credential.username + credential.status + credential.link
			const normalizedText = UtilsMixins.methods.normalizeText(searchText)
			const normalizedSearch = UtilsMixins.methods.normalizeText(text)
			return normalizedText.includes(normalizedSearch)
		}) })
    },
    getRecentAccessedCredentials(limit=5) {
        function _sortLastAccessed(a, b) {
            if (a.last_accessed > b.last_accessed) {
                return 1;
            }
            if (a.last_accessed < b.last_accessed) {
                return -1;
            }
            return 0
        }
        let orderedCredentials = credentials.sort(_sortLastAccessed).slice(0, limit)
        return mockasync({ credentials:  orderedCredentials })
    },
    getNumberOfCredentials() {
        return mockasync({ count_credentials: credentials.length })
    },
    toggleCredentialFavorite(credential) {
        return mockasync({ credential })
    },
    getCredentialPassword(credentialId) {
        const password = passwords.find(password => password.id === credentialId).password
        return mockasync({ password })
    },
    deleteCredentialPassword(credentialId) {
        for (let index = 0; index < passwords.length; index++) {
            const credential = passwords[index]
            if (credential.id === credentialId) {
                passwords.splice(index, 1)
                break
            }
        }
        return mockasync({})
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
        return mockasync({ credential: newCredential })
    },

    // Logs
    getAllLogs() {
        return mockasync({ logs })
    },

    // PassImage
    getPassImage (userEmail) {
        return mockasync({ image_url })
    }
};

export default api;
