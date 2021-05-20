import logTypes from '@/helpers/LogTypes'
import { credentials } from './DB_Credentials'

export const logs = [
    {
        id: 1,
        credential: {
            id: credentials[0].id,
            name: credentials[0].name,
            active: credentials[0].active
        },
        user_id: 1,
        type: logTypes.CREDENTIAL_CREATION,
        created_at: new Date()
    },
    {
        id: 2,
        credential: {
            id: credentials[1].id,
            name: credentials[1].name,
            active: credentials[1].active
        },
        user_id: 1,
        type: logTypes.CREDENTIAL_CREATION,
        created_at: new Date()
    },
    {
        id: 3,
        credential: {
            id: credentials[2].id,
            name: credentials[2].name,
            active: credentials[2].active
        },
        user_id: 1,
        type: logTypes.CREDENTIAL_CREATION,
        created_at: new Date()
    }
]