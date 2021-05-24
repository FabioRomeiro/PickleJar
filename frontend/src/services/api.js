import { get, post } from '../helpers/Http';

const api = {
    login(email, data){
        return post('/api/login', {
            email,
            pass_data: JSON.stringify({
                grid_size: data.gridSize,
                coords: data.inputs
            })
        })
    },
    logout(){
        return post('/api/logout');
    },
    whoami(){
        return get('/api/whoami');
    },
    add_todo(newtask){
        return post('/api/add_todo', {new_task: newtask});
    },
    list_todos(){
        return get('/api/list_todos');
    },

    // Credentials
    getAllCredentials() {
        return get('/api/credentials')
    },
    getFavoriteCredentials() {
        return get('/api/credentials', { favorite_only: true })
    },
    getCredentialByText(search_text) {
        return get('/api/credentials', { search_text })
    },
    getRecentAccessedCredentials(limit=5) {
        return get('/api/credentials', { order_by: '-last_accessed' })
    },
    getNumberOfCredentials() {
        return get('/api/credentials', { count_only: true })
    },
    toggleCredentialFavorite(credential) {
        return post('/api/credentials/save', {
            ...credential,
            favorite: !credential.favorite
        })
    },
    getCredentialPassword(credential_id) {
        return get('/api/credentials/password', { credential_id })
    },
    deleteCredentialPassword(id) {
        return post('/api/credentials/delete', { id })
    },
    saveCredential(credential) {
        return post('/api/credentials/save', credential)
    },

    // Logs
    getAllLogs() {
        return get('/api/logs')
    },

    // PassImage
    getPassImage (userEmail) {
        return get('/api/passimage', {
            user_email: userEmail
        })
    }
}
export default api;
