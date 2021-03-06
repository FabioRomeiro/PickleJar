<template>
    <div class="overview">
        <div class="overview__content">
            <div class="body-item">
                <Card headerTitle="Favoritas" headerIcon="grade">
                    <template v-slot:content>
                        <ul class="overview__credentials"> 
                            <li class="credentials-item" v-for="credential in favoriteCredentials" :key="credential.id">
                                <CredentialItem :credential="credential" />
                            </li>

                            <EmptyCasePlaceholder
                                v-if="!favoriteCredentials.length"
                                title="Nenhuma credencial favorita"
                                description="Clique sobre a imagem da credencial para marca-la como favorita."
                            >
                                <CredentialItem mock />
                            </EmptyCasePlaceholder>
                        </ul>
                    </template>
                </Card>
            </div>

            <div class="body-item">
                <Card headerTitle="Acessadas recentemente" headerIcon="schedule">
                    <template v-slot:content>
                        <ul class="overview__credentials"> 
                            <li class="credentials-item" v-for="credential in recentAccessedCredentials" :key="credential.id">
                                <CredentialItem :credential="credential" />
                            </li>
                            <EmptyCasePlaceholder
                                v-if="!recentAccessedCredentials.length"
                                title="Sem registro de acesso"
                                description="Você não tem nenhuma credencial registrada ainda."
                                icon="filter_list"
                            />
                        </ul>
                    </template>
                    <template v-slot:footer>
                        <router-link to="/logs" class="link">
                            <i class="material-icons">toc</i>
                            <span>Veja todas as suas atividades</span>
                        </router-link>
                    </template>
                </Card>

                <div class="overview__all-credentials">
                    <router-link to="/credentials" class="link">
                        <span>Acessar <strong>{{ numberOfCredentials }} credenciais</strong></span>
                        <i class="material-icons">keyboard_arrow_right</i>
                    </router-link>
                </div>
            </div>
        </div>

        <CustomButton rounded @click="openCredentialCreation" class="overview__add-button">
            <i class="material-icons">add</i>
        </CustomButton>
    </div>
</template>


<script>
import EmptyCasePlaceholder from '@/components/Utils/EmptyCasePlaceholder.vue'
import Card from '@/components/Utils/Card.vue'
import CustomButton from '@/components/Forms/CustomButton.vue'
import CredentialItem from '@/components/Credential/CredentialItem.vue'

export default {
    name: 'Overview',
    components: {
        EmptyCasePlaceholder,
        CredentialItem,
        Card,
        CustomButton
    },
    async created() {
        await this.$store.dispatch('credentials/getFavoriteCredentials')
        await this.$store.dispatch('credentials/getRecentAccessedCredentials', 5)
        await this.$store.dispatch('credentials/getNumberOfCredentials')
    },
    computed: {
        favoriteCredentials() {
            return this.$store.getters['credentials/favoriteCredentials']
        },
        numberOfCredentials() {
            return this.$store.getters['credentials/numberOfCredentials']
        },
        recentAccessedCredentials() {
            return this.$store.getters['credentials/recentAccessedCredentials'](5)
        }
    },
    data() {
        return {}
    },
    methods: {
        openCredentialCreation() {
            this.$eventBus.emit(this.$eventKeys.ADD_CREDENTIAL)
        }
    },
}
</script>

<style lang="scss" scoped>
    .overview {
        display: flex;
        flex-direction: column;
        align-items: center;

        &__credentials {
            .credentials-item {
                margin-bottom: spacing(2);

                &:last-child {
                    margin-bottom: 0;
                }
            }
        }

        &__content {
            display: flex;
            margin: -#{spacing(1)};

            .body-item {
                margin: spacing(1);
            }
        }

        &__all-credentials {
            font-size: 24px;
            color: $color-green-dark;
            height: 100px;
            display: flex;
            align-items: center;
            justify-content: center;

            .link {
                
                font-weight: $font-weight-regular;
                display: flex;
                align-items: center;

                i {
                margin-left: spacing(1);
                margin-right: 0;
                font-size: 34px;
                }
            }
        }

        &__add-button {
            position: fixed;
            right: 80px;
            bottom: 80px;
            font-size: 30px;
        }
    }
</style>