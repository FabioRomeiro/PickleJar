<template>
    <ListingSection class="logs" headerTitle="Suas atividades" headerIcon="toc">
        <template v-slot:headerButtons>
            <CustomButton class="header-button" variant="neutral" @click="$router.push({name: 'Overview'})">
                Voltar
            </CustomButton>
        </template>
        <template v-slot:filters>
            <div class="listing-filter">
                <span class="label">Credencial</span>
                <CustomSelect
                    v-model="credentialId"
                    :options="credentialOptions"
                    :disabled="isFilteredByProfileLogType"
                />
            </div>
            <div class="listing-filter">
                <span class="label">Tipo de registro</span>
                <CustomSelect
                    v-model="logType"
                    :options="logTypes"
                />
            </div>
        </template>
        <template v-slot:content>
            <table class="logs__table">
                <thead>
                    <tr class="logs__item logs__item--header">
                        <th class="logs__col logs__col--time">Momento</th>
                        <th class="logs__col logs__col--message">Ocorrido</th>
                        <th class="logs__col logs__col--useragent">Acessado de</th>
                        <th class="logs__col logs__col--credential">Credencial</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="logs__item" v-for="log in filteredLogs" :key="log.id">
                        <td class="logs__col logs__col--time">
                            {{ accessDate(log.created_at) }}
                        </td>
                        <td class="logs__col logs__col--message">
                            <p>
                                {{ getLogMessage(log.type) }}
                            </p>
                        </td>
                        <td class="logs__col logs__col--useragent">
                            {{ getReadableUseragent(log.useragent) }}
                        </td>
                        <td class="logs__col logs__col--credential">
                            <a
                                v-if="log.credential"
                                href
                                @click.prevent="openCredential(log.credential)"
                                class="item-credential"
                                :class="{'item-credential-deleted': !log.credential.active}"
                            >
                                {{ log.credential.name }}
                            </a>
                        </td>
                    </tr>
                </tbody>
            </table>
            <EmptyCasePlaceholder
                v-if="!filteredLogs.length"
                title="Nenhum registro foi encontrado"
                description="Tente outra combinação de filtro para obter diferentes resultados"
                icon="filter_list"
            />
        </template>
    </ListingSection>
</template>

<script>
import ListingSection from '@/components/Utils/ListingSection.vue'
import EmptyCasePlaceholder from '@/components/Utils/EmptyCasePlaceholder.vue'
import CustomButton from '@/components/Forms/CustomButton.vue'
import CustomSelect from '@/components/Forms/CustomSelect.vue'
import logTypes from '@/helpers/LogTypes'
import UAParser from 'ua-parser-js'
import { UtilsMixins } from '@/helpers/Mixins'

export default {
    name: 'Credentials',
    components: {
        ListingSection,
        EmptyCasePlaceholder,
        CustomButton,
        CustomSelect
    },
    async created() {
        await this.$store.dispatch('credentials/getAllCredentials')
        await this.$store.dispatch('logs/getAllLogs')
    },
    mixins: [UtilsMixins],
    computed: {
        logs() {
            return this.$store.getters['logs/logs']
        },
        filteredLogs() {
            function sortAlgorithm(a, b) {
                if (a.createdAt > b.createdAt) {
                    return -1
                }
                if (a.createdAt < b.createdAt) {
                    return 1
                }
                return 0
            }

            let filteredLogs = this.logs
            
            if (this.credentialId !== 'ALL') {
                filteredLogs = filteredLogs.filter(log => log.credential_id == this.credentialId)
            }

            filteredLogs = filteredLogs.filter(log => log.type === this.logType || this.logType === 'ALL')
            
            return filteredLogs.sort(sortAlgorithm)
        },
        isFilteredByProfileLogType() {
            return this.logTypes.includes(this.logType);
        },
        credentialOptions() {
            let credentials = this.$store.getters['credentials/credentials']
                .map(credential => ({ value: credential.id, label: credential.name }));

            return [
                { value: 'ALL', label: 'All' },
                ...credentials
            ];
        },
        logTypes() {
            return [
                { value: 'ALL', label: 'All' },
                { 
                    value: logTypes.PASSWORD_ACCESS, 
                    label: 'Password access', 
                    disabled: !this.hasLogWithLogType(logTypes.PASSWORD_ACCESS)
                },
                { 
                    value: logTypes.CREDENTIAL_CREATION, 
                    label: 'Credential creation', 
                    disabled: !this.hasLogWithLogType(logTypes.CREDENTIAL_CREATION)
                },
                { 
                    value: logTypes.CREDENTIAL_EDITING, 
                    label: 'Credential editing', 
                    disabled: !this.hasLogWithLogType(logTypes.CREDENTIAL_EDITING)
                },
                { 
                    value: logTypes.ACCOUNT_LOGIN, 
                    label: 'Account login', 
                    disabled: !this.hasLogWithLogType(logTypes.ACCOUNT_LOGIN)
                },
                { 
                    value: logTypes.ACCOUNT_LOGOUT, 
                    label: 'Account logout', 
                    disabled: !this.hasLogWithLogType(logTypes.ACCOUNT_LOGOUT)
                },
                { 
                    value: logTypes.CREDENTIAL_DELETE, 
                    label: 'Credential delete', 
                    disabled: !this.hasLogWithLogType(logTypes.CREDENTIAL_DELETE)
                },
                { 
                    value: logTypes.ACCOUNT_ACCESS, 
                    label: 'Account access', 
                    disabled: !this.hasLogWithLogType(logTypes.ACCOUNT_ACCESS)
                },
            ]
        },
    },
    methods: {
        getLogMessage(logType) {
            switch (logType) {
                case logTypes.PASSWORD_ACCESS:
                    return 'Acessou a senha da credencial'
                case logTypes.CREDENTIAL_CREATION:
                    return 'Criou nova credencial'
                case logTypes.CREDENTIAL_EDITING:
                    return 'Editou informações da credencial'
                case logTypes.ACCOUNT_LOGIN:
                    return 'Entrou na conta'
                case logTypes.ACCOUNT_LOGOUT:
                    return 'Saiu da conta'
                case logTypes.CREDENTIAL_DELETE:
                    return 'Deletou a credencial'
                case logTypes.ACCOUNT_ACCESS:
                    return 'Acessou a conta'
            }
        },
        hasLogWithLogType(type) {
            return this.logs.some(log => log.type === type)
        },
        getReadableUseragent(userAgent) {
            let parsedUa = new UAParser(userAgent);
            let device = parsedUa.getDevice().model;
            let browser = parsedUa.getBrowser().name;
            let os = parsedUa.getOS().name;
            return `${device ? device + ' - ' : '' }${browser} - ${os}`;
        },
        getCredential(credentialId) {
            return this.$store.getters['credentials/credentialById'](credentialId)
        },
        openCredential(credential) {
            if (!credential.active) {
                return
            }
            this.$eventBus.emit(this.$eventKeys.VIEW_CREDENTIAL, this.getCredential(credential.id));
        }
    },
    data() {
        return {
            credentialId: 'ALL',
            logType: 'ALL'
        }
    }
}
</script>

<style lang="scss" scoped>
    .logs {
        $this: &;

        &__table {
            width: 100%;
            margin: spacing(3) 0;
        }

        &__item {
            &--header {
                font-size: 16px;
                font-weight: $font-weight-semibold;
                border-bottom: solid 1px $color-green;
            }
        }

        &__col {
            text-align: left;
            padding: spacing(2);

            &--time {
                max-width: 20%;
            }

            &--credential {
                .item-credential {
                    &.item-credential-deleted {
                        color: $color-gray-dark;
                        cursor: default;
                        pointer-events: none;
                    }
                }
            }
        }
    }
</style>