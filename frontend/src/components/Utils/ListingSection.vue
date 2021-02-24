<template>
    <div class="listing-section">
        <div class="listing-section__header">
            <h3 class="listing-section__title">
                <i class="material-icons icon">{{ headerIcon }}</i>
                <span>{{ headerTitle }}</span>
            </h3>
            <div class="listing-section__actions">
                <slot name="headerButtons" ></slot>
            </div>
        </div>
        <div class="listing-section__filters">
            <slot name="filters" ></slot>
        </div>
        <div class="listing-section__content">
            <slot name="content"></slot>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ListingSection',
    props: {
        headerTitle: String,
        headerIcon: String
    }
}
</script>

<style lang="scss">
    .listing-section__filters {
        display: flex;
        align-items: center;
        
        .listing-filter {
            display: flex;
            align-items: center;
            margin-right: spacing(3);

            .label {
                margin-right: spacing(1);
                font-weight: $font-weight-medium;
                color: $color-gray-dark;
            }
        }
    }

    .listing-section__header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        
        .header-button {
            margin-right: spacing(2);

            &:last-child {
                margin-right: 0;
            }
        }
    }

</style>

<style lang="scss" scoped>
.listing-section {

    &__title {
        font-size: 24px;
        font-weight: $font-weight-medium;
        display: inline-flex;
        align-items: center;
        position: relative;
        margin-bottom: spacing(3);

        &::after {
            content: '';
            position: absolute;
            width: 100%;
            height: 2px;
            border-radius: 3px;
            background-color: rgba($color-green-dark, 1);
            box-shadow: 0 0 3px $color-green, 0 0 2px inset $color-green;
            left: 0;
            bottom: -#{spacing(1)};
        }

        .icon {
            margin-right: spacing(1);
            color: $color-green-dark;
            filter: drop-shadow(0 0 2px rgba($color-green, .5));
        }
    }

    &__actions {
        
        .action-button {
            margin-right: spacing(2);

            &:last-child {
                margin-right: 0;
            }
        }
    }
}
</style>