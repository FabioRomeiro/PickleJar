<template>
    <a href @click.prevent="openCredential()" class="credential-search-item">
        <ImageReplace class="credential-search-item__picture" :src="credential.image" :name="credential.name" />
        <span class="credential-search-item__name">
            {{ credential.name }}
        </span>
    </a>
</template>

<script>
import ImageReplace from '@/components/Utils/ImageReplace.vue'

export default {
    name: 'CredentialSearchItem',
    props: {
        credential: Object
    },
    components: {
        ImageReplace
    },
    methods: {
        openCredential() {
            this.$eventBus.emit(this.$eventKeys.VIEW_CREDENTIAL, this.credential)
            this.$emit('click', this.credential.id)
        }
    }
}
</script>

<style lang="scss" scoped>
    .credential-search-item {
        padding: spacing(1) spacing(2);
        flex-grow: 1;

        &:hover {
            background-color: $color-green-extra-light;
        }

        &__picture {
            width: 53px;
            height: 40px;
            margin-right: spacing(2);
            border-radius: 3px;
        }
    }
</style>