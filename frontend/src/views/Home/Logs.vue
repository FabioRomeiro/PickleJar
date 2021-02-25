<template>
    <ListingSection class="logs" headerTitle="Your activities" headerIcon="toc">
        <template v-slot:headerButtons>
            <CustomButton class="header-button" variant="neutral" @click="$router.push('/')">
                Voltar
            </CustomButton>
        </template>
        <template v-slot:filters>
            <div class="listing-filter">
                <span class="label">Credential</span>
                <CustomSelect
                    v-model="credentialId"
                    :options="credentialOptions"
                    :disabled="isFilteredByProfileLogType"
                />
            </div>
            <div class="listing-filter">
                <span class="label">Log type</span>
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
                        <th class="logs__col logs__col--time">Time</th>
                        <th class="logs__col logs__col--message">Occurred</th>
                        <th class="logs__col logs__col--useragent">Accessed from</th>
                        <th class="logs__col logs__col--credential">Credential</th>
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
                            <a href @click.prevent="openCredential(log.credential_id)" class="item-credential" v-if="log.credential_id">
                                {{ getCredential(log.credential_id).name }}
                            </a>
                        </td>
                    </tr>
                </tbody>
            </table>
            <EmptyCasePlaceholder
                v-if="!filteredLogs.length"
                title="No activity were found"
                description="You might try another filter combination to get different results"
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
                    value: logTypes.CREDENTIAL_COPY, 
                    label: 'Credential copy', 
                    disabled: !this.hasLogWithLogType(logTypes.CREDENTIAL_COPY)
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
                    return 'Accessed the credential\'s password'
                case logTypes.CREDENTIAL_CREATION:
                    return 'Created new credential'
                case logTypes.CREDENTIAL_EDITING:
                    return 'Edited credential informations'
                case logTypes.ACCOUNT_LOGIN:
                    return 'Logged in the account'
                case logTypes.ACCOUNT_LOGOUT:
                    return 'Logged out of the account'
                case logTypes.CREDENTIAL_DELETE:
                    return 'Deleted credential'
                case logTypes.CREDENTIAL_COPY:
                    return 'Copied the credential\' password to the clipboard'
                case logTypes.ACCOUNT_ACCESS:
                    return 'Accessed the account using a browser'
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
        openCredential(credentialId) {
            this.$eventBus.emit(this.$eventKeys.VIEW_CREDENTIAL, this.getCredential(credentialId));
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
        }
    }
</style>