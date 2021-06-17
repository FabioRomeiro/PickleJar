<template>
    <ListingSection class="credentials" headerTitle="Credenciais" headerIcon="lock">
        <template v-slot:headerButtons>
            <CustomButton class="header-button" variant="neutral" @click="$router.push('/')">
                Voltar
            </CustomButton>
            <CustomButton class="credentials__header-button" @click="addNewCredential()">
                Adicionar credencial
            </CustomButton>
        </template>
        <template v-slot:filters>
            <div class="listing-filter">
                <span class="label">Ordenar por</span>
                <CustomSelect
                    v-model="sortBy"
                    :options="sortOptions"
                />
            </div>
            <div class="listing-filter">
                <CustomCheckbox
                    v-model="favoritesOnly"
                    label="Apenas favoritas"
                />
            </div>
        </template>
        <template v-slot:content>
            <ul class="credentials__list">
                <li class="credentials__item" v-for="credential in filteredCredentials" :key="credential.id">
                    <CredentialCard :credential="credential" />
                </li>
                <li class="credentials__empty-message" v-if="!filteredCredentials.length">
                    <EmptyCasePlaceholder
                        title="Nenhuma credencial encontrada"
                        description="Tente outra combinação de filtro para encontrar o que precisa."
                    >
                        <CredentialCard mock />
                    </EmptyCasePlaceholder>
                </li>
            </ul>
        </template>
    </ListingSection>
</template>

<script>
import ListingSection from '@/components/Utils/ListingSection.vue'
import EmptyCasePlaceholder from '@/components/Utils/EmptyCasePlaceholder.vue'
import CredentialCard from '@/components/Credential/CredentialCard.vue'
import CustomButton from '@/components/Forms/CustomButton.vue'
import CustomCheckbox from '@/components/Forms/CustomCheckbox.vue'
import CustomSelect from '@/components/Forms/CustomSelect.vue'

export default {
    name: 'Credentials',
    components: {
        ListingSection,
        EmptyCasePlaceholder,
        CredentialCard,
        CustomCheckbox,
        CustomButton,
        CustomSelect
    },
    async created() {
        await this.$store.dispatch('credentials/getAllCredentials');
    },
    computed: {
        credentials() {
            return this.$store.getters['credentials/credentials']
        },
        filteredCredentials() {
            let filtered = this.credentials
            if (this.favoritesOnly) {
               filtered = filtered.filter(credential => credential.favorite)
            }
            if (this.credentialStatus) {
                filtered = filtered.filter(credential => credential.status === this.credentialStatus)
            }
            
            const sortProperty = {
                'created': 'created_at',
                'access': 'last_access'
            }[this.sortBy]
            
            function sortAlgorithm(a, b) {
                if (a[sortProperty] > b[sortProperty]) {
                    return 1
                }
                if (a[sortProperty] < b[sortProperty]) {
                    return -1
                }
                return 0
            }

            filtered = filtered.sort(sortAlgorithm)

            return filtered
        }
    },
    methods: {
        addNewCredential() {
            this.$eventBus.emit(this.$eventKeys.ADD_CREDENTIAL)
        }
    },
    data() {
        return {
            favoritesOnly: false,
            sortOptions: [
                { value: 'creation', label: 'Criação' },
                { value: 'access', label: 'Acesso' },
            ],
            sortBy: 'access',
            credentialStatus: '',
            statusOptions: [
                { value: '', label: 'All' },
                { value: 'STRONG', label: 'Forte' },
                { value: 'MEDIUM', label: 'Moderada' },
                { value: 'UNSAFE', label: 'Insegura' },
                { value: 'OBVIOUS', label: 'Óbvia' },
            ]
        }
    }
}
</script>

<style lang="scss" scoped>
    .credentials {
        width: 100%;

        &__list {
            display: flex;
            margin-top: spacing(3);
        }

        &__empty-message {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: spacing(7);
            width: 100%;
        }

        &__item {
            margin-right: spacing(2);
        }
    }
</style>