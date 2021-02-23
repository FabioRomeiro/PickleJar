import store from '@/store/index.js'
import { copy } from '@/helpers/ClipBoard.js'

export const CredentialMixins = {
    methods: {
        async toggleFavorite(credential) {
            const newState = await store.dispatch('credentials/toggleCredentialFavorite', credential)
            return newState
        },
        async copyPassword(credentialId) {
            const password = await store.dispatch('credentials/getCredentialPassword', credentialId)
            copy(password)
        }
    }
}

export const UtilsMixins = {
    methods: {
        accessDate(value) {
            function forceTwoChars(number) {
                return ("0" + number).slice(-2);
            }
          
            function getTimeByDay(unity, dayMs) {
                return Math.ceil({
                    'sec': dayMs * 24 * 60 * 60, 
                    'min': dayMs * 24 * 60, 
                    'hour': dayMs * 24 
                }[unity]);
            }
          
            const today = new Date();
            const date = new Date(value);
            const msInADay = 1000 * 60 * 60 * 24;
            const difference = (today.getTime() - date.getTime()) / msInADay;
          
            if (difference >= 1) {
          
                let day = forceTwoChars(date.getDate());
                let month = forceTwoChars(date.getMonth() + 1);
                let year = date.getFullYear();
                
                return `${month}/${day}/${year}`;
            }
            else if (difference >= 0.06) {
                return `${getTimeByDay('hour', difference)} hours ago`;
            }
            else if (difference >= 0.0006) {
                return `${getTimeByDay('min', difference)} minutes ago`;
            }
            else {
                return `${getTimeByDay('sec', difference)} seconds ago`;
            }
        }
    }
}