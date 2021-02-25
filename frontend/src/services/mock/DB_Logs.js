import logTypes from '@/helpers/LogTypes'

export const logs = [
    {
        id: 1,
        credential_id: 1,
        user_id: 1,
        type: logTypes.CREDENTIAL_CREATION,
        created_at: new Date()
    },
    {
        id: 2,
        credential_id: 2,
        user_id: 1,
        type: logTypes.CREDENTIAL_CREATION,
        created_at: new Date()
    },
    {
        id: 3,
        credential_id: 3,
        user_id: 1,
        type: logTypes.CREDENTIAL_CREATION,
        created_at: new Date()
    }
]