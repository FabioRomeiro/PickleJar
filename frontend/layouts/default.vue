<template>
  <div>
    <toolbar />
    <nuxt></nuxt>
  </div>
</template>

<script>
  import toolbar from '~/components/toolbar.vue'
  export default {
    components: {
      toolbar
    },
    data: () => ({
      layout: {
        drawer: true,
      },
    }),
    computed: {
      snack () {
        return this.$store.getters.snack
      }
    }
  }
</script>