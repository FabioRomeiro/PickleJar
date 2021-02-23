<template>
    <button
        :disabled="disabled"
        class="custom-button"
        :type="type"
        :class="getClasses()"
    >
        <slot></slot>
    </button>
</template>

<script>
export default {
    name: 'CustomButton',
    props: {
        rounded: Boolean,
        disabled: Boolean,
        type: {
            type: String,
            default: 'button'
        },
        variant: String
    },
    methods: {
        getClasses() {
            const base = 'custom-button--';
            let variant = base + this.variant
            let conditional = { 
                'custom-button--rounded': this.rounded 
            };

            return [variant, conditional];
        }
    }
}
</script>

<style lang="scss" scoped>
    .custom-button {
        border: none;
        background-color: $color-green;
        color: white;
        padding: spacing(1);
        border-radius: 3px;
        font-family: 'Work Sans', sans-serif;
        font-weight: $font-weight-semibold;
        cursor: pointer;
        box-shadow: shadow-depth(1);
        transition: background-color .2s ease-in-out, 
                    box-shadow .2s ease-in-out;

        &:disabled {
            background-color: $color-gray;
            box-shadow: none;
            cursor: default;
        }

        &--rounded {
            border-radius: 50%;
            width: 60px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 0;
        }

        &--neutral {
            background-color: white;
            border: solid 1px $color-green;
            color: $color-green;
        }

        &--danger {
            background-color: $color-red;
            color: white;
            border: solid 1px $color-red-dark;
        }
    }
</style>