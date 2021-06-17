<template>
    <div class="credential-search" v-click-outside="closeSearchResults">
        <CustomInput 
            class="credential-search__input" 
            type="search"
            variant="big"
            v-model="search"
            @input="searchCredentials"
            @focus="searchFocused"
            placeholder="Procure pelo nome ou url de uma credencial"
        />

        <div class="credential-search__results" v-if="searchResultsOpen">
            <ul class="credential-search__list">
                <li 
                    v-for="credential in filteredCredentials" 
                    :key="credential.id" 
                    class="credential-search__item"
                >
                    <CredentialSearchItem :credential="credential" @click="closeSearchResults" />
                </li>
            </ul>
            
            <div 
                class="credential-search__result-message" 
                v-if="(!filteredCredentials.length && !loading && !debounce) || loading"
            >
                <EmptyCasePlaceholder
                    v-if="!filteredCredentials.length && !loading && !debounce"
                    title="Nenhuma credencial encontrada"
                    description="Tente buscar por outro texto"
                    icon="filter_list"
                />
                <EmptyCasePlaceholder
                    title="Carregando credenciais"
                    description="Sua busca estará pronta em um instante"
                    v-if="loading"
                />
            </div>
        </div>
    </div>
</template>

<script>
import CustomInput from '@/components/Forms/CustomInput.vue'
import CredentialSearchItem from '@/components/Toolbar/CredentialSearchItem.vue'
import EmptyCasePlaceholder from '@/components/Utils/EmptyCasePlaceholder.vue'
import ClickOutside from 'vue-click-outside'
import { UtilsMixins } from '@/helpers/Mixins'

export default {
    name: 'CredentialSearch',
    components: {
        CustomInput,
        CredentialSearchItem,
        EmptyCasePlaceholder
    },
    mixins: [UtilsMixins],
    directives: {
        ClickOutside
    },
    computed: {
        credentials() {
            return this.$store.getters['credentials/credentials']
        },
        filteredCredentials() {
            const normalizedSearch = this.normalizeText(this.search)
            return this.credentials.filter(credential => {
                const credentialText = credential.name + credential.username + credential.status + credential.link
                const normalizedCredentialText = this.normalizeText(credentialText)
                return normalizedCredentialText.includes(normalizedSearch)
            })
        }
    },
    methods: {
        searchCredentials(text) {
            clearTimeout(this.debounce)
            if (!text) {
                return this.closeSearchResults()
            }

            this.openSearchResults()

            this.loading = true
            this.debounce = setTimeout(() =>{
                this.$store.dispatch('credentials/getCredentialByText', text)
                    .then(() => this.loading = false)
                this.debounce = null
            }, 500)
        },
        searchFocused() {
            if (this.search) {
                this.openSearchResults()
            }
        },
        closeSearchResults() {
            this.searchResultsOpen = false
        },
        openSearchResults() {
            this.searchResultsOpen = true
        }
    },
    data() {
        return {
            search: '',
            debounce: null,
            loading: false,
            searchResultsOpen: false
        }
    }
}
</script>

<style lang="scss" scoped>
    .credential-search {
        position: relative;

        &__results {
            position: absolute;
            width: 100%;
            max-height: 300px;
            overflow-y: auto;
            background-color: white;
            box-shadow: shadow-depth(3);
            border-radius: 3px;
            z-index: 2;
            box-sizing: border-box;
        }

        &__list {
            display: flex;
            flex-direction: column;
        }

        &__item {
            display: flex;
            border-bottom: 1px solid $color-green-extra-light;

            &:last-child {
                border-bottom: none;
            }
        }

        &__input {
            width: 100%;
        }

        &__result-message {
            padding: spacing(2) 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
    }
</style>