<template>
    <div class="workspace-form">
        <CustomInput 
            @input="updateCredentialField($event, 'name')"
            id="credential-name" 
            class="workspace-form__field" 
            :modelValue="credential.name" 
            label="Password name:"
        />
        <CustomInput 
            @input="updateCredentialField($event, 'username')"
            id="credential-username" 
            class="workspace-form__field" 
            :modelValue="credential.username" 
            label="Username:"
        />

        <div class="workspace-form__field-wrapper">
            <CustomInput 
                @input="updatePassword"
                id="credential-password" 
                class="workspace-form__field" 
                :modelValue="password"
                :type="passwordVisible ? 'text' : 'password'"
                label="Password:"
            />
            <CustomButton @click="togglePassword" class="workspace-form__preview-btn">
                <i class="material-icons">visibility</i>
            </CustomButton>
        </div>
        <CustomCheckbox
            @input="updateCredentialField($event, 'favorite')"
            class="workspace-form__field" 
            :modelValue="credential.favorite" 
            label="Favorite" 
        />
        <CustomInput 
            @input="updateCredentialField($event, 'link')"
            id="credential-url" 
            class="workspace-form__field" 
            :modelValue="credential.link" 
            label="Website URL:"
        />
        <CustomInput 
            @input="updateCredentialField($event, 'image')"
            id="credential-image" 
            class="workspace-form__field" 
            :modelValue="credential.image" 
            label="Website image:"
        />
        <CustomInput 
            @input="updateCredentialField($event, 'notes')"
            id="credential-note" 
            class="workspace-form__field" 
            :modelValue="credential.notes" 
            label="Notes:"
        />
    </div>
</template>

<script>
import CustomInput from '@/components/Forms/CustomInput.vue'
import CustomCheckbox from '@/components/Forms/CustomCheckbox.vue'
import CustomButton from '@/components/Forms/CustomButton.vue'

export default {
    name: 'WorkspaceForm',
    components: {
        CustomInput,
        CustomCheckbox,
        CustomButton
    },
    computed: {
        credential() {
            return this.$store.getters['credentialWorkspace/credential']
        },
        password() {
            return this.$store.getters['credentialWorkspace/password']
        }
    },
    methods: {
        togglePassword() {
            this.passwordVisible = !this.passwordVisible;
        },
        updateCredentialField(value, field) {
            this.$store.commit('credentialWorkspace/SET_CREDENTIAL_FIELD', {field, value})
            this.saveCredentialWithPassword()
        },
        updatePassword(value) {
            this.$store.commit('credentialWorkspace/SET_PASSWORD', value)
            this.saveCredentialWithPassword()
        },
        saveCredentialWithPassword() {
            clearTimeout(this.savingTimeout)
            this.savingTimeout = setTimeout(() => {
                let data = {...this.credential}
                if (this.password) {
                    data.password = this.password
                }
                this.$store.dispatch('credentials/saveCredential', data)
            }, 1000)
        }
    },
    data() {
        return {
            passwordVisible: false,
            savingTimeout: null
        }
    }
}
</script>

<style lang="scss" scoped>
    .workspace-form {
        
        &__field {
            margin-bottom: spacing(1);
            flex-grow: 1;

            &:last-child {
                margin-bottom: 0;
            }
        }
        
        &__field-wrapper {
            display: flex;
            align-items: center;
        }

        &__preview-btn {
            margin: 10px 0 0 spacing(1);
        }
    }
</style>