<template>
    <div
        class="credential-card" 
        :class="{
            'credential-card--mock': mock,
            'credential-card--favorite': credential.favorite
        }"
    >
        <a 
            class="credential-card__content"
            href 
            @click.prevent="openPasswordWorkspace('view')"
        >
            <div class="credential-card__pic" :class="{ 'has-content': !!credential.image || !!credential.name }">
                <ImageReplace class="picture" :src="credential.image" :name="credential.name" />
            </div>
            
            <div class="credential-card__info">
                <span class="title-wrapper">
                    <a @click.stop.prevent="togglePasswordFavoriteState" href>
                        <i class="material-icons icon">grade</i>
                    </a>
                    <span class="title" :class="{ 'has-content': !!credential.name }">
                        {{ credentialName }}
                    </span>
                </span>
                <span class="access" :class="{ 'has-content': !!credential.last_accessed }">
                    <span v-if="credential.last_accessed">
                        Acessado a {{ accessDate(credential.last_accessed) }}
                    </span>
                </span>
            </div>
        </a>

        <div class="credential-card__actions">
            <a @click.prevent="openPasswordWorkspace('edit')" href class="credential-card__action" title="Edit password">
                <i class="material-icons icon">edit</i>
            </a>
            <a href @click.prevent="copyPassword(credential.id)" class="credential-card__action" title="Copy password">
                <i class="material-icons icon">filter_none</i>
            </a>
            <a 
                :href="credential.link"
                target="_blank" 
                class="credential-card__action" 
                :class="{ 'credential-card__action--disabled': !credential.link }" 
                title="Access link"
            >
                <i class="material-icons icon">open_in_new</i>
            </a>
            <a href @click.prevent="deleteCredential" class="credential-card__action credential-card__action--delete" title="Delete password">
                <i class="material-icons icon">delete</i>
            </a>
        </div>
    </div>
</template>

<script>
import ImageReplace from '@/components/Utils/ImageReplace.vue';
import { UtilsMixins, CredentialMixins } from '@/helpers/Mixins.js';

export default {
    name: 'CredentialCard',
    props: {
        credential: {
            type: Object,
            default: () => ({})
        },
        mock: Boolean,
    },
    components: {
        ImageReplace
    },
    mixins: [CredentialMixins, UtilsMixins],
    computed: {
        credentialName() {
            if (this.credential.name) {
                return this.credential.name
            }
            if (!this.mock) {
                return 'Nova credencial'
            }
            return ''
        }
    },
    methods: {
        deleteCredential() {
            this.$store.dispatch('credentials/deleteCredential', this.credential)
            this.$eventBus.emit(this.$eventKeys.CALL_ALERT, {
                message: 'Credencial deletada com sucesso',
                type: 'success',
                lifeTime: 4000
            })
        },
        togglePasswordFavoriteState() {
            if (this.mock) {
                return
            }
            this.toggleFavorite(this.credential)
        },
        openPasswordWorkspace(mode) {
            switch (mode) {
                case 'view':
                    this.$eventBus.emit(this.$eventKeys.VIEW_CREDENTIAL, this.credential)
                    break;
                case 'edit':
                    this.$eventBus.emit(this.$eventKeys.EDIT_CREDENTIAL, this.credential)
                    break
            }
        }
    }
}
</script>

<style lang="scss" scoped>
    .credential-card {
        $card-measure: 176px;
        $this: &;

        display: flex;
        align-items: center;
        flex-direction: column;
        width: $card-measure;
        height: $card-measure;
        background-color: white;
        border-radius: 4px;
        box-shadow: shadow-depth(2);
        cursor: default;

        &__pic,
        &__info {
            cursor: pointer;
        }

        &__pic {

            $pic-height: 60px;
            $pic-width: 100%;

            display: block;
            margin-bottom: spacing(1);
            width: $pic-width;
            height: $pic-height;
            overflow: hidden;
            border-radius: 3px;
            cursor: pointer;
            position: relative;

            .picture {
                min-height: $pic-height;
                max-height: $pic-height;
                width: 100%;
                object-fit: cover;
            }
        }

        &__info {
            display: flex;
            flex-direction: column;
            width: 100%;
            height: 44px;

            .title-wrapper {

                font-size: 16px;
                font-weight: $font-weight-medium;
                margin-bottom: 4px;
                display: flex;
                align-items: center; 
                width: 100%;

                .title {
                    max-width: 100%;
                    overflow: hidden;
                    text-overflow: ellipsis;
                    flex-grow: 1;
                    white-space: nowrap;
                }
                
                .icon {
                    margin-right: spacing(1);
                    font-size: 20px;
                    color: $color-gray-light;
                    transition: color .2s ease-in-out;
                }
            }
    
            .link {
                font-size: 12px;
                font-weight: $font-weight-light;
                text-decoration: none;
                color: $color-gray;
                margin-bottom: 2px;
            }
    
            .access {
                font-size: 12px;
                color: $color-gray;
            }
        }

        &__actions {
            height: 38px;
            display: flex;
            width: $card-measure;
            position: relative;
        }

        &__action {
            height: 100%;
            width: 25%;
            background-color: rgba($color-green-light, .1);
            border-top: solid 1px $color-green-light;
            box-sizing: border-box;
            display: flex;
            align-items: center;
            justify-content: center;
            color: $color-green-light;
            cursor: pointer;

            .icon {
                margin: 0;
                font-size: 20px;
            }

            &:first-child {
                border-radius: 0 0 0 4px;
            }
            &:last-child {
                border-radius: 0 0 4px 0;
            }

            &:hover {
                color: $color-green;
                background-color: rgba($color-green-light, .3);
            }

            &--delete {
                &:hover {
                    background-color: $color-red-extra-light;
                    color: $color-red;
                }
            }

            &--disabled {
                background-color: $color-gray-extra-light;
                pointer-events: none;
                color: $color-gray;
                cursor: default;
            }
        }

        &__content {
            display: flex;
            flex-direction: column;
            height: 122px;
            padding: spacing(1);
            width: calc(100% - #{spacing(1)} * 2);
        }

        &--favorite {
            #{$this}__info {
                
                .title-wrapper {
                    .icon {
                        color: $color-yellow;
                    }
                }
            }
        }

        &--mock {

            pointer-events: none;
            cursor: default;

            #{$this}__pic:not(.has-content) {
                background-color: $color-gray;
                
                .picture {
                    display: none;
                }
            }

            #{$this}__info {

                .title:not(.has-content),
                .access:not(.has-content) {
                    &::after {
                        content: '';
                        display: block;
                        background-color: $color-gray-light;
                        border-radius: 2px;
                    }
                }

                .title {
                    &::after {
                        width: 100%;
                        height: 14px;
                        background-color: $color-gray;
                    }
                }

                .access {
                    &::after {
                        width: 90%;
                        height: 10px;
                    }
                }
            }

            #{$this}__action {
                background-color: rgba($color-gray, .1);
                border-color: $color-gray;

                .icon {
                    position: relative;
                    color: rgba(0,0,0,0);

                    &::after {
                        content: '';
                        position: absolute;
                        top: 0;
                        left: 0;
                        width: 20px;
                        height: 20px;
                        border-radius: 3px;
                        background-color: $color-gray-light;
                    }
                }
            }
        }
    }
</style>