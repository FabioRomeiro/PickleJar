<template>
    <div class="card">
        <div class="card__header">
            <div class="header-title">
                <i class="header-icon material-icons">{{ headerIcon }}</i>
                <h5>{{ headerTitle }}</h5>
            </div>
        </div>
        <div class="card__content" v-if="$slots.content">
            <slot name="content"></slot>
        </div>
        <div class="card__footer" v-if="$slots.footer">
            <slot name="footer"></slot>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Card',
    props: {
        headerIcon: String,
        headerTitle: String
    }
}
</script>

<style lang="scss" scoped>
.card {
    background-color: white;
    width: 400px;
    box-shadow: shadow-depth(1);
    border-radius: 3px; 

    &__header {
        padding: 0 spacing(3);
        height: 53px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: solid 1px #DBFDDF;

        .header-title {
            display: flex;
            align-items: center;
            font-size: 16px;
            font-weight: $font-weight-medium;

            .header-icon {
                width: 16px;
                margin-right: spacing(2);
            }
        }
    }

    &__content {
        padding: spacing(2) spacing(3);
    }

    &__footer {
        height: 46px;
        display: flex;
        align-items: center;
        padding: 0 spacing(3);

        &--dark {
            background-color: $color-gray-extra-light;
            border-top: solid 1px $color-gray-light;
        }
    }
}
</style>