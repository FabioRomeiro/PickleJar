from django.db.models import Q

from core.models import Credential


def save_credential(credential_dict, owner):
    id = credential_dict.get('id')
    if id:
        credential = Credential.objects.get(pk=id)
        credential.name = credential_dict.get('name', '')
        credential.username = credential_dict.get('username', '')
        credential.password = credential_dict.get('password', '')
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
    else:
        credential_dict.update({'owner': owner})
        Credential.objects.create(**credential_dict)


def delete_credential(id, owner):
    Credential.objects.filter(pk=id, owner=owner).delete()


def list_credentials(owner=None, search_text='', order_by='-created_at', favorite_only=False, count_only=False,
                     descending=False):
    credentials_qs = Credential.objects.filter(owner=owner).order_by(order_by)

    if favorite_only:
        credentials_qs = credentials_qs.filter(favorite=True)

    if search_text:
        search = Q(name__contains=search_text) | Q(username__contains=search_text) | Q(link__contains=search_text)
        credentials_qs = credentials_qs.filter(search)

    if count_only:
        return credentials_qs.count()

    return [credential.to_dict_json() for credential in credentials_qs]
