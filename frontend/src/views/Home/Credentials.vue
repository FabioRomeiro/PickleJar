<template>
    <ListingSection class="credentials" headerTitle="Credentials" headerIcon="lock">
        <template v-slot:headerButtons>
            <CustomButton class="credentials__header-button" variant="neutral" @click="$router.push('/')">
                Voltar
            </CustomButton>
            <CustomButton class="credentials__header-button" @click="addNewCredential()">
                Add Credential
            </CustomButton>
        </template>
        <template v-slot:filters>
            <div class="credentials__filter">
                <span class="label">Credential status</span>
                <CustomSelect
                    v-model="credentialStatus"
                    :options="statusOptions"
                />
            </div>
            <div class="credentials__filter">
                <span class="label">Sort by</span>
                <CustomSelect
                    v-model="sortBy"
                    :options="sortOptions"
                />
            </div>
            <div class="credentials__filter">
                <CustomCheckbox
                    v-model="favoritesOnly"
                    label="Favorites only"
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
                        title="No credentials were found"
                        description="Try another filter combination to find exactly what you need."
                        :condition="true"
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
            return this.$store.getters['credentials/credentials'] || []
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
                { value: 'creation', label: 'Creation' },
                { value: 'access', label: 'Access' },
            ],
            sortBy: 'access',
            credentialStatus: '',
            statusOptions: [
                { value: '', label: 'All' },
                { value: 'STRONG', label: 'Strong' },
                { value: 'MEDIUM', label: 'Moderate' },
                { value: 'UNSAFE', label: 'Unsafe' },
                { value: 'OBVIOUS', label: 'Obvious' },
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

        &__filter {
            display: flex;
            align-items: center;
            margin-right: spacing(3);

            .label {
                margin-right: spacing(1);
                font-weight: $font-weight-medium;
                color: $color-gray-dark;
            }
        }

        &__header-button {
            margin-right: spacing(2);

            &:last-child {
                margin-right: 0;
            }
        }
    }
</style>