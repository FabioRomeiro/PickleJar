<template>
  <div></div>
</template>

<script>
  import Vuex from 'vuex'
  import Snacks from '~/helpers/Snacks.js'
  import AppApi from '~apijs'
  export default {
    components: {},
    computed: Object.assign(
      {},
      Vuex.mapGetters([
        'logged_user'
      ])
    ),
    methods: {
      open_login_dialog (evt) {
        this.$refs.login_dialog.open();
        evt.stopPropagation();
      },
      logout(){
        AppApi.logout().then(()=>{
          this.$store.commit('SET_LOGGED_USER', null);
          Snacks.show(this.$store, {text: 'Até logo!'})
        });
      }
    }
  }
</script>