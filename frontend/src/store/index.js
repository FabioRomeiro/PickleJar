import Vuex from 'vuex'
import credentials from './modules/credentials'

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    credentials
  },
  strict: debug
})
