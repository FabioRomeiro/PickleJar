# coding: utf-8
import json
from django.http.response import HttpResponse, JsonResponse
from django.contrib import auth
from commons.django_model_utils import get_or_none
from commons.django_views_utils import ajax_login_required
from django.views.decorators.csrf import csrf_exempt
from core.service import credential_svc, log_svc


def dapau(request):
    raise Exception('break on purpose')


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


def logout(request):
    if request.method.lower() != 'post':
        raise Exception('Logout only via post')
    if request.user.is_authenticated():
        log_svc.log_logout(request.user)
    auth.logout(request)
    return HttpResponse('{}', content_type='application/json')


def whoami(request):
    i_am = {
        'user': _user2dict(request.user),
        'authenticated': True,
    } if request.user.is_authenticated else {'authenticated': False}
    return JsonResponse(i_am)


@ajax_login_required
def save_credential(request):
    credential = request.POST.dict()
    user = request.user
    updated_credential = credential_svc.save_credential(credential, user)
    return JsonResponse({'credential': updated_credential})


@ajax_login_required
def delete_credential(request):
    id = request.POST.get('id')
    user = request.user
    credential_svc.delete_credential(id, user)
    return JsonResponse({})


@ajax_login_required
def list_credentials(request):
    params = request.GET.dict()
    user = request.user
    params['owner'] = user
    result = credential_svc.list_credentials(**params)
    if params.get('count_only'):
        return JsonResponse({'count_credentials': result})
    return JsonResponse({'credentials': result})


@ajax_login_required
def get_password(request):
    params = request.GET.dict()
    user = request.user
    params['owner'] = user
    password = credential_svc.get_password(**params)
    return JsonResponse({'password': password})


def list_logs(request):
    logs = log_svc.list_logs(request.user)
    return JsonResponse({'logs': logs})


def _user2dict(user):
    d = {
        'id': user.id,
        'name': user.get_full_name(),
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'permissions': {
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }
    return d
