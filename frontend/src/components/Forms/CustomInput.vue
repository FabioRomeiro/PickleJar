<template>
    <div class="custom-input">
        <label v-if="label" :for="id" class="custom-input__label">{{ label }}</label>
        
        <input
            :id="id"
            class="custom-input__input"
            :class="`custom-input__input--${variant}`"
            @input.stop="$emit('input', $event.target.value)"
            @focus.stop="$emit('focus', $event.target.value)"
            :type="type" 
            :placeholder="placeholder"
            :value="value"
        />
        
        <i 
            v-if="type === 'search'" 
            class="material-icons custom-input__search-icon"
        >
            search
        </i>
    </div>
</template>

<script>
export default {
    name: 'CustomInput',
    props: {
        variant: {
            type: String,
            default: 'normal'
        },
        type: String,
        label: String,
        placeholder: String,
        id: String,
        value: [String, Number]
    }
}
</script>

<style lang="scss">
    .custom-input {

        position: relative;
        display: flex;
        flex-direction: column;

        &__label {
            display: block;
            margin-bottom: 4px;
        }

        &__input {
            padding: spacing(1);
            border: none;
            font-family: 'Work Sans', sans-serif;
            border-radius: 4px;
            font-size: 14px;
            border: solid 1px $color-green-light;

            &::placeholder {
                color: $color-gray;
            }

            &[type=search] {
                padding-left: spacing(5);
            }

            &--big {
                padding: 12px spacing(2);
            }
        }

        &__search-icon {
            position: absolute;
            top: 8px;
            left: 8px;
            color: $color-green-dark;
            font-size: 26px;
        }
    }
</style>