<template>
    <div class="credential-workspace" v-if="credential">
        <Card class="credential-workspace__wrapper" :headerTitle="headerTitle" :headerIcon="headerIcon" noContentPadding>
            <template v-slot:headerButtons>
                <CustomButton 
                    v-if="isEditing || isViewing"
                    @click="deleteCredential" 
                    variant="danger"
                >
                    Delete
                </CustomButton>
            </template>
            <template v-slot:content>
                <div class="credential-workspace__content">
                    <div class="credential-workspace__preview">
                        <CredentialCard :credential="credential" mock />
                    </div>

                    <WorkspaceCredentialForm 
                        class="credential-workspace__form" 
                        v-if="isEditable"
                    />

                    <WorkspaceCredentialPresentation
                        v-else
                        class="credential-workspace__presentation"
                    />
                </div>
            </template>
            <template v-slot:footer>
                <div class="credential-workspace__footer">
                    <CustomButton class="footer-button" @click="openWorkspaceToEdit(credential)" v-if="isViewing">
                        Edit
                    </CustomButton>
                    <CustomButton class="footer-button" variant="neutral" @click="closeWorkspace">
                        Close
                    </CustomButton>
                </div>
            </template>
        </Card>
        <div @click="closeWorkspace" class="credential-workspace__shadow"></div>
    </div>
</template>

<script>
import Card from '@/components/Utils/Card.vue'
import WorkspaceCredentialPresentation from '@/components/CredentialWorkspace/WorkspaceCredentialPresentation.vue'
import WorkspaceCredentialForm from '@/components/CredentialWorkspace/WorkspaceCredentialForm.vue'
import CustomButton from '@/components/Forms/CustomButton.vue'
import CredentialCard from '@/components/Credential/CredentialCard.vue'

export default {
    name: 'CredentialWorkspace',
    components: { 
        Card, 
        WorkspaceCredentialPresentation, 
        WorkspaceCredentialForm, 
        CustomButton, 
        CredentialCard 
    },
    created() {
        this.$eventBus.on(this.$eventKeys.ADD_CREDENTIAL, this.createCredentialAndOpenWorkspace, true)
        this.$eventBus.on(this.$eventKeys.EDIT_CREDENTIAL, this.openWorkspaceToEdit, true)
        this.$eventBus.on(this.$eventKeys.VIEW_CREDENTIAL, this.openWorkspaceToView, true)

        const self = this
        const ws = new WebSocket('ws://localhost:8000/ws/credentials/')
		ws.onmessage = evt => {
			const data = JSON.parse(evt.data)
            if (data.type === 'send_updated_credential') {
                self.$store.commit('credentials/ADD_CREDENTIALS', [data.credential])   
            }
            else if (data.type === 'send_deleted_credential') {
                self.$store.commit('credentials/REMOVE_CREDENTIAL', data.credential_id)
            }
		}
    },
    computed: {
        headerTitle() {
            if (this.isEditing) {
                return `Editing ${this.credential.name ? `- ${this.credential.name}` : ''}`
            }
            return this.credential.name
        },
        headerIcon() {
            if (this.isEditing) {
                return 'edit'
            }
            return 'lock'
        },
        isEditable() {
            return this.$store.getters['credentialWorkspace/editMode']
        },
        isEditing() {
            return this.isEditable && !!this.credential.id
        },
        isViewing() {
            return !this.isEditable && this.credential.id
        },
        credential() {
            return this.$store.getters['credentialWorkspace/credential']
        }
    },
    methods: {
        async createCredentialAndOpenWorkspace() {
            let credential = await this.$store.dispatch('credentials/saveCredential', {
                name: '',
                username: '',
                password: ''
            })
            credential = this.$store.getters['credentials/credentialById'](credential.id)
            this.openWorkspaceToEdit(credential)
        },
        async openWorkspaceToEdit(credential) {
            let password = await this.$store.dispatch('credentials/getCredentialPassword', credential.id)
            this.$store.commit('credentialWorkspace/SET_PASSWORD', password)
            this.$store.commit('credentialWorkspace/OPEN_WORKSPACE', {
                credential,
                editMode: true
            })
        },
        openWorkspaceToView(credential) {
            this.$store.commit('credentialWorkspace/OPEN_WORKSPACE', {
                credential,
                editMode: false
            })
        },
        deleteCredential() {
            if (!this.credential) {
                return
            }
            this.$store.dispatch('credentials/deleteCredential', this.credential)
            this.closeWorkspace()
        },
        closeWorkspace() {
            this.$store.commit('credentialWorkspace/CLOSE_WORKSPACE')
        }
    }
}
</script>

<style lang="scss" scoped>
    .credential-workspace {
        position: fixed;
        left: 0;
        top: 0;
        width: 100vw;
        height: 100vh;
        display: flex;
        justify-content: center;
        z-index: 1;

        &__wrapper {
            margin-top: 5%;
            align-self: baseline;
            z-index: 1;
        }

        &__preview {
            background-color: $color-green;
            padding: spacing(2) 0;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        &__form,
        &__presentation {
            max-height: 35vh;
            overflow-y: auto;
            padding: spacing(2) spacing(3);
        }

        &__footer {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;

            .footer-button {
                margin: 0 spacing(2);
            }
        }
        
        &__shadow {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,.5);
            z-index: 0;
        }
    }
</style>