<template>
    <div class="empty-case-placeholder">
        <slot>
            <i class="material-icons empty-case-placeholder__icon" v-if="icon">
                {{ icon }}
            </i>
        </slot>
        <p 
            class="empty-case-placeholder__title"
            :class="{ 'empty-case-placeholder__title--with-spacing': $slots.default || icon }"
        >
            {{ title }}
        </p>
        <p class="empty-case-placeholder__description">{{ description }}</p>
    </div>
</template>

<script>
export default {
    name: 'EmptyCasePlaceholder',
    props: {
        title: String,
        description: String,
        icon: String
    }
}
</script>

<style lang="scss" scoped>
    .empty-case-placeholder {

        color: $color-gray-dark;
        display: flex;
        flex-direction: column;
        align-items: center;

        &__icon {
            font-size: 50px;
            height: 50px;
        }

        &__title,
        &__description {
            text-align: center;
        }

        &__description {
            margin-top: spacing(1);
        }

        &__title {
            font-weight: $font-weight-semibold;

            &--with-spacing {
                margin-top: spacing(2);
            }
        }
    }
</style>