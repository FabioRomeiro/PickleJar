from core.models import ActivityLog


PASSWORD_ACCESS = 'PASSWORD_ACCESS'
CREDENTIAL_CREATION = 'CREDENTIAL_CREATION'
CREDENTIAL_EDITING = 'CREDENTIAL_EDITING'
CREDENTIAL_DELETE = 'CREDENTIAL_DELETE'
ACCOUNT_LOGIN = 'ACCOUNT_LOGIN'
ACCOUNT_LOGOUT = 'ACCOUNT_LOGOUT'
ACCOUNT_ACCESS = 'ACCOUNT_ACCESS'


def log_login(user):
    logs = ActivityLog(
        type=ACCOUNT_LOGIN,
        logged_user=user,
    )
    logs.save()


def log_logout(user):
    logs = ActivityLog(
        type=ACCOUNT_LOGOUT,
        logged_user=user,
    )
    logs.save()


def log_password_access(user, credential):
    logs = ActivityLog(
        type=PASSWORD_ACCESS,
        logged_user=user,
        credential=credential
    )
    logs.save()


def log_credential_creation(user, credential):
    logs = ActivityLog(
        type=CREDENTIAL_CREATION,
        logged_user=user,
        credential=credential
    )
    logs.save()


def log_credential_edit(user, credential):
    logs = ActivityLog(
        type=CREDENTIAL_EDITING,
        logged_user=user,
        credential=credential
    )
    logs.save()


def log_credential_delete(user, credential):
    logs = ActivityLog(
        type=CREDENTIAL_DELETE,
        logged_user=user,
        credential=credential
    )
    logs.save()


def list_logs(user):
    logs_qs = (ActivityLog.objects
               .filter(logged_user=user,
                       type__in=[PASSWORD_ACCESS, CREDENTIAL_CREATION, CREDENTIAL_EDITING,
                                 CREDENTIAL_DELETE, ACCOUNT_LOGIN, ACCOUNT_LOGOUT, ACCOUNT_ACCESS])
               .order_by('-created_at'))
    logs = []
    for log in logs_qs:
        log_dict = {'id': log.id, 'type': log.type, 'created_at': log.created_at}
        if log.credential:
            log_dict['credential'] = {
                'id': log.credential.id,
                'name': log.credential.name,
                'active': log.credential.active
            }
        logs.append(log_dict)
    return logs
