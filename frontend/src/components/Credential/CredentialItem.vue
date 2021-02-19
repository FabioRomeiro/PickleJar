<template>
    <div class="credential-item" :class="{ 'credential-item--mock': mock }">
        <a href @click.prevent="openCredential" class="credential-item__content">
            <a
                href
                @click.prevent.stop="toggleCredentialFavoriteState"
                class="credential-item__pic" 
                :class="variations"
            >
                <div class="favorite-cover">
                    <i class="material-icons icon">grade</i>
                </div>
                <ImageReplace class="picture" :src="credential.image" :name="credential.name" />
            </a>

            <div class="credential-item__info">
                <p class="info-title">
                    {{ credential.name }}
                </p>
                <a 
                    :href="credential.link" 
                    target="_blank" 
                    class="info-link" 
                >
                    {{ credential.link }}
                </a>
                <span href class="info-access">
                    <span v-if="!mock">
                        Accessed at {{ accessDate(credential.lastAccess) }}
                    </span>
                </span>
            </div>
        </a>

        <div class="credential-item__actions">
            <a
                :href="credential.link"
                target="_blank"
                class="action-button"
                :class="{ 'disabled': !credential.link }"
            >
                <i class="material-icons icon">open_in_new</i>
            </a>
            <a href @click.prevent="copyPassword(credential.id)" class="action-button">
                <i class="material-icons icon">filter_none</i>
            </a>
        </div>
    </div>
</template>

<script>
import ImageReplace from '@/components/Utils/ImageReplace.vue'; 
import { CredentialMixins, UtilsMixins } from '@/helpers/Mixins.js';

export default {
    name: 'CredentialItem',
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
    computed: {
        variations() {
            return { 
                'credential-item__pic--favorite': this.credential.favorite,
                'credential-item__pic--mock': this.mock 
            }
        }
    },
    mixins: [CredentialMixins, UtilsMixins],
    methods: {
        toggleCredentialFavoriteState() {
            if (this.mock) {
                return;
            }

            this.toggleFavorite(this.credential);
        },
        openCredential() {
            if (this.mock) {
                return;
            }

            // EventBus.$emit(EventBus.events.VIEW_PASSWORD, this.credential.id);
        }
    }
}
</script>

<style lang="scss" scoped>
    .credential-item {
        $this: &;

        display: flex;
        align-items: center;
        justify-content: space-between;

        &__pic {

            $pic-height: 50px;
            $pic-width: 63px;

            display: block;
            margin-right: spacing(1);
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

            .favorite-cover {
                opacity: 0;
                width: 100%;
                height: 100%;
                background: linear-gradient(
                    309.46deg, 
                    rgba(255, 255, 255, 0.78) -4.69%, 
                    rgba(255, 255, 255, 0.71) 25.3%, 
                    rgba(255, 255, 255, 0) 77.65%);
                position: absolute;
                top: 0;
                left: 0;
                display: flex;
                align-items: flex-end;
                justify-content: flex-end;
                transition: opacity .2s ease-in-out;
                z-index: 1;

                .icon {
                    font-size: 16px;
                    color: $color-yellow;
                    margin: 5px;
                }
            }

            &:hover {
                .favorite-cover {
                    opacity: 1;
                }
            }

            &--favorite {
                .favorite-cover {
                    opacity: 1;
                    background: linear-gradient(
                        309.46deg, 
                        rgba(255, 229, 0, 0.53) -4.69%, 
                        rgba(255, 229, 0, 0.41) 25.3%, 
                        rgba(255, 229, 0, 0) 77.65%);    
                }
            }

            &--mock {

                pointer-events: none;
                cursor: default;

                .favorite-cover {
                    opacity: 1;
                    background-color:$color-gray;

                    .icon {
                        color: $color-gray;
                    }
                }
            }

        }

        &__info {
            display: flex;
            flex-direction: column;

            .info-title {
                font-size: 16px;
                font-weight: $font-weight-medium;
                margin-bottom: 4px;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                max-width: 20ch;
            }
    
            .info-link {
                font-size: 12px;
                font-weight: $font-weight-light;
                text-decoration: none;
                color: $color-gray;
                margin-bottom: 2px;
            }
    
            .info-access {
                font-size: 12px;
                color: $color-gray;
            }
        }

        &__content {
            display: flex;
            align-items: center;
        }

        &__actions {
            display: flex;
            align-items: center;
            
            .action-button {
                margin: 0 spacing(1);
                font-size: 18px;

                &:last-child {
                    margin-right: 0;
                }

                .icon {
                    margin: 0;
                }

                &.disabled {
                    color: $color-gray;
                }
            }
        }

        &--mock {

            #{$this}__content {
                pointer-events: none;
            }

            #{$this}__info {
                .info-title, 
                .info-link, 
                .info-access {
                    &::after {
                        content: '';
                        display: block;
                        background-color: $color-gray-light;
                        border-radius: 2px;
                    }
                }
    
                .info-title {
                    &::after {
                        width: 70px;
                        height: 14px;
                        background-color: $color-gray;
                    }
                }
                
                .info-link {
                    &::after {
                        width: 100px;
                        height: 10px;
                    }
                }
    
                .info-access {
                    &::after {
                        width: 80px;
                        height: 10px;
                    }
                }
            }
            
            #{$this}__actions {
                .action-button {
                    
                    position: relative;
                    pointer-events: none;

                    &:after {
                        content: '';
                        width: 20px;
                        height: 20px;
                        border-radius: 3px;
                        background-color: $color-gray-light;
                        position: absolute;
                        left: 0;
                        top: 0;
                    }
                }
            }
        }
    }    
</style>