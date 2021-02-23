<template>
    <div class="custom-select">
        <label v-if="label" :for="id" class="custom-select__label">{{ label }}</label>
        <select 
            class="custom-select__select" 
            :id="id"
            @input="$emit('input', $event.target.value)"
            :value="value"
            :disabled="disabled"
        >
            <option v-for="option in options" :key="option.value" :value="option.value" :disabled="option.disabled">
                {{ option.label || option.value }}
            </option>
        </select>
    </div>
</template>

<script>
export default {
    name: 'CustomInput',
    props: {
        label: String,
        id: String,
        value: String,
        disabled: Boolean,
        emptyOption: {
            type: String,
            default: 'Select an option'
        },
        options: {
            type: Array,
            default() { return []; },
            validator: options =>  !options.length || options.every(
                option => ![null, undefined].includes(option.value))
        }
    }
}
</script>

<style lang="scss">
    .custom-select {

        &__select {
            padding: 8px spacing(1);
            border: none;
            font-family: 'Work Sans', sans-serif;
            border-radius: 4px;
            border: solid 1px $color-green;
            font-size: 14px;
            width: 100%;
        }
    }
</style>