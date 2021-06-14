<template>
  <div class="password-input">
    <CustomInput type="password" label="Senha" @input="onInput"/>
    <div v-if="showStrength" class="password-input__strength-status">
      Sua senha está: <span class="strenght-label" :class="getStrengthClass()">{{ strengthStatus }}</span>
    </div>
  </div>
</template>

<script>
import CustomInput from '@/components/Forms/CustomInput'

export default {
  props: {
		modelValue: String,
    showStrength: Boolean
  },
  components: {
    CustomInput
  },
  computed: {
    strength () {
      let total = 0
      if (/[a-z]/.test(this.modelValue)) {
        total += 1
      }
      if (/[A-Z]/.test(this.modelValue)) {
        total += 1
      }
      if (/\d/.test(this.modelValue)) {
        total += 1
      }
      if (/[ `!@#$%^&*()_+\-=[\]{};':"\\|,.<>/?~]/.test(this.modelValue)) {
        total += 1
      }
      if (this.modelValue.length >= 8) {
        total += 1
      }
      return total
    },
    strengthStatus () {
      if (this.strength <= 3) {
        return 'Fraca'
      }
      if (this.strength <= 4) {
        return 'Moderada'
      }
      return 'Forte'
    }
  },
  methods: {
    getStrengthClass () {
      return `strenght-label-${this.strengthStatus.toLowerCase()}`
    },
    onInput (e) {
      this.$emit('input', this.strength)
      this.$emit('update:modelValue', e)
    }
  }
}
</script>

<style lang="scss" scoped>
.password-input {
  &__strength-status {
    margin-top: spacing(2);

    .strenght-label {
      font-weight: 500;

      &.strenght-label-fraca {
        color: $color-red;
      }

      &.strenght-label-moderada {
        color: $color-yellow;
      }

      &.strenght-label-forte {
        color: $color-green-dark;
      }
    }
  }
}
</style>