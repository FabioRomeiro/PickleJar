<template>
  <button type="button" @click="entrar">Entrar</button>
</template>

<script>
import api from 'Apijs'

export default {
  methods: {
    entrar() {
      api.login('teste', 'um2345678')
    }
  }
}
</script>