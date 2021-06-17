<template>
    <div class="workspace-credential-presentation">
        <a
            :href="credential.link" 
            target="_blank" 
            class="workspace-credential-presentation__info-field workspace-credential-presentation__info-field--horizontal" 
            v-if="credential.link"
        >
            <span class="field-value">
                <i class="material-icons icon">open_in_new</i>
                <span>{{ credential.link }}</span>
            </span>
        </a>

        <div class="workspace-credential-presentation__info-field workspace-credential-presentation__info-field--horizontal">
            <span class="field-label">Ultimo acesso:</span>
            <span class="field-value">{{ accessDate(credential.last_accessed) }}</span>
        </div>

        <div class="workspace-credential-presentation__info-field">
            <span class="field-label">Nome da credencial:</span>
            <span class="field-value">{{ credential.name }}</span>
        </div>

        <div class="workspace-credential-presentation__info-field workspace-credential-presentation__info-field--actions">
            <span class="field-label">Username:</span>
            <span class="field-value">
                <span class="value-text">{{ credential.username }}</span>
                <div class="value-actions">
                    <CustomButton class="value-button" @click="copyUsername">
                        <i class="material-icons">filter_none</i>
                    </CustomButton>
                </div>
            </span>
        </div>

        <div class="workspace-credential-presentation__info-field workspace-credential-presentation__info-field--actions">
            <span class="field-label">Senha:</span>
            <span class="field-value">
                <span class="value-text">{{ passwordText }}</span>
                <div class="value-actions">
                    <CustomButton class="value-button" @click="togglePassword">
                        <i class="material-icons">visibility</i>
                    </CustomButton>
                    <CustomButton class="value-button" @click="copyPassword">
                        <i class="material-icons">filter_none</i>
                    </CustomButton>
                </div>
            </span>
        </div>
        <div class="workspace-credential-presentation__info-field" v-if="credential.notes">
            <span class="field-label">Notas:</span>
            <span class="field-value">{{ credential.notes }}</span>
        </div>
    </div>
</template>

<script>
import { UtilsMixins } from '@/helpers/Mixins.js'
import { copy } from '@/helpers/ClipBoard.js'
import CustomButton from '@/components/Forms/CustomButton.vue'

export default {
    name: 'WorkspacePasswordPresentation',
    components: {
        CustomButton
    },
    data() {
        return {
            showPassword: false
        }
    },
    mixins: [UtilsMixins],
    computed: {
        credential() {
            return this.$store.getters['credentialWorkspace/credential']
        },
        password() {
            return this.$store.getters['credentialWorkspace/password']
        },
        passwordText() {
            if (!this.showPassword) {
                return '●●●●●●●●●●●'
            }

            return this.password
        }
    },
    methods: {
        copyUsername() {
            copy(this.credential.username)
        },
        async togglePassword() {
            if (this.showPassword) {
                this.showPassword = false
                return
            }
            if (!this.password) {
                await this.getPassword()
            }
            this.showPassword = true
        },
        async copyPassword() {
            if (!this.password) {
                await this.getPassword()
            }
            copy(this.password)
        },
        async getPassword() {
            const password = await this.$store.dispatch('credentials/getCredentialPassword', this.credential.id)
            this.$store.commit('credentialWorkspace/SET_PASSWORD', password)
        }
    }
}
</script>

<style lang="scss" scoped>
    .workspace-credential-presentation {

        &__info-field {

            display: flex;
            flex-direction: column;
            margin-bottom: spacing(2);

            &:last-child {
                margin-bottom: 0;
            }

            .field-label {
                margin-bottom: 4px;
                font-weight: $font-weight-semibold;
                color: $color-green-dark;
            }

            .field-value {
                font-size: 16px;
            }

            &--horizontal {
                flex-direction: row;

                .field-label {
                    margin-bottom: 0;
                    margin-right: spacing(1);
                }

                .field-value {
                    
                    display: flex;
                    align-items: center;

                    .icon {
                        font-size: 16px;
                        margin-right: spacing(1);
                    }
                }
            }

            &--actions {

                .field-value {

                    display: flex;
                    justify-content: space-between;
                    align-items: center;

                    .value-actions {
                        .value-button {
                            margin-left: spacing(1);
                        }
                    }
                }
            }
        }
    }
</style>