import { credentials, passwords } from './mock/DB_Credentials.js'

var logged_user = null;

function mockasync (data) {
  return new Promise((resolve) => {
    setTimeout(() => resolve({data: data}), 600)
  })
}

const api = {
    login(username, password){
        if(password){
            logged_user = {
                username: username,
                first_name: 'Mark',
                last_name: 'Zuckerberg',
                email: 'zuck@facebook.com',
                notifications_enabled: true,
                permissions:{
                    ADMIN: username == 'admin',
                    STAFF: username == 'admin',
                }
            };
        }
        return mockasync(logged_user);
    },
    logout(){
        logged_user = null;
        return mockasync({});
    },
    whoami(){
        return mockasync(logged_user ? {
            authenticated: true,
            user: logged_user,
        } : {authenticated: false});
    },

    // Credentials
    getFavoriteCredentials() {
        console.log(credentials)
        return mockasync(credentials).then(res => res.data)
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
        console.log(orderedCredentials)
        return mockasync(orderedCredentials).then(res => res.data)
    },
    getNumberOfCredentials() {
        console.log(credentials.length)
        return mockasync(credentials.length).then(res => res.data)
    },
    toggleCredentialFavorite(credentialId) {
        const credential = credentials.find(credential => credential.id === credentialId)
        console.log(!credential.favorite)
        return mockasync(!credential.favorite).then(res => res.data)
    },
    getCredentialPassword(credentialId) {
        const password = passwords.find(password => password.id === credentialId).password
        return mockasync(password).then(res => res.data)
    }
};

export default api;
