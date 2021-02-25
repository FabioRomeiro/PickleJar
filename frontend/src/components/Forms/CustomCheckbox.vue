<template>
    <label :for="id" class="custom-checkbox">
        <input
            :id="id"
            class="custom-checkbox__input" 
            @change="$emit('update:modelValue', $event.target.checked)"
            type="checkbox"
            :checked="modelValue"
        />
        
        <div class="custom-checkbox__box"></div>

        <span class="custom-checkbox__label">
            {{ label }}
        </span>
    </label>
</template>

<script>
export default {
    name: 'CustomInput',
    props: {
        label: String,
        id: String,
        modelValue: Boolean
    }
}
</script>

<style lang="scss">
    .custom-checkbox {

        position: relative;
        cursor: pointer;
        display: flex;
        align-items: center;

        &__box {
            width: 14px;
            height: 14px;
            background-color: white;
            border-radius: 3px;
            border: solid 1px $color-green;
            transition: background-color .2s ease-in-out, border-color .2s ease-in-out;
            position: relative;

            &::after,
            &::before {
                content: '';
                position: absolute;
                width: 8px;
                height: 2px;
                border-radius: 3px;
                background-color: white;
            }

            &::after {
                transform: rotate(45deg);
                width: 5px;
                top: 7px;
                left: 2px;
            }

            &::before {
                transform: rotate(-45deg);
                top: 6px;
                left: 4px;
            }
        }

        &__label {
            margin-left: 6px;
            margin-bottom: 2px;
            user-select: none;
        }

        &__input {
            position: absolute;
            opacity: 0;

            &:checked {
                + .custom-checkbox__box {
                    background-color: $color-green;
                    border-color: $color-green-dark;
                }
            }
        }
    }
</style>