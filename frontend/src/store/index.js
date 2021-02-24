import Vuex from 'vuex'
import credentials from './modules/credentials'
import credentialWorkspace from './modules/credentialWorkspace'
import logs from './modules/logs'

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    credentials,
    credentialWorkspace,
    logs
  },
  strict: debug
})
