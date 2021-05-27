from django.db.models import Q
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from core.models import Credential
from core.service import log_svc


def save_credential(credential_dict, owner):
    id = credential_dict.get('id')
    credential_dict['favorite'] = credential_dict.get('favorite') == 'true'
    if id:
        credential = Credential.objects.get(pk=id)
        credential.name = credential_dict.get('name', '')
        credential.username = credential_dict.get('username', '')
        new_password = credential_dict.get('password')
        if new_password:
            credential.password = new_password
        credential.image = credential_dict.get('image', '')
        credential.link = credential_dict.get('link', '')
        credential.notes = credential_dict.get('notes', '')
        credential.favorite = credential_dict.get('favorite', False)
        # credential.status = credential_dict.get('status')
        credential.active = credential_dict.get('active', True)
        credential.owner = owner
        # credential.last_updated = credential_dict.get('last_updated')
        # credential.last_accessed = credential_dict.get('last_accessed')
        credential.save()
        log_svc.log_credential_edit(owner, credential)
    else:
        credential_dict.update({'owner': owner})
        credential = Credential.objects.create(**credential_dict)
        log_svc.log_credential_creation(owner, credential)

    credential_dict = credential.to_dict_json()
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('credentials', {
        'type': 'send_updated_credential',
        'credential': credential_dict,
        'credential_id': credential.id
    })
    return credential_dict


def delete_credential(id, owner):
    credential = Credential.objects.filter(pk=id, owner=owner)
    if credential.exists():
        log_svc.log_credential_delete(owner, credential[0])
        credential.update(active=False)


def list_credentials(owner=None, search_text='', order_by='-created_at', favorite_only=False, count_only=False,
                     descending=False):
    credentials_qs = Credential.objects.filter(owner=owner, active=True).order_by(order_by)

    if favorite_only:
        credentials_qs = credentials_qs.filter(favorite=True)

    if search_text:
        search = Q(name__contains=search_text) | Q(username__contains=search_text) | Q(link__contains=search_text)
        credentials_qs = credentials_qs.filter(search)

    if count_only:
        return credentials_qs.count()

    return [credential.to_dict_json() for credential in credentials_qs]


def get_password(owner=None, credential_id=None):
    credential = Credential.objects.get(owner=owner, pk=credential_id, active=True)
    log_svc.log_password_access(owner, credential)
    return credential.password

