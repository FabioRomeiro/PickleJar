<template>
    <div class="listing-section">
        <PageHeader :icon="headerIcon" :title="headerTitle">
            <slot name="headerButtons" ></slot>
        </PageHeader>
        <div class="listing-section__filters">
            <slot name="filters" ></slot>
        </div>
        <div class="listing-section__content">
            <slot name="content"></slot>
        </div>
    </div>
</template>

<script>
import PageHeader from '@/components/Utils/PageHeader.vue'

export default {
    name: 'ListingSection',
    props: {
        headerTitle: String,
        headerIcon: String
    },
    components: {
        PageHeader
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
</style>
