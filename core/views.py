# coding: utf-8
import json
from django.http.response import HttpResponse, JsonResponse
from django.contrib import auth
from commons.django_views_utils import ajax_login_required
from django.views.decorators.csrf import csrf_exempt
from core.service import credential_svc, log_svc, passimage_svc, auth_svc


def dapau(request):
    raise Exception('break on purpose')


@csrf_exempt
def login(request):
    email = request.POST['email']
    confirm_user = request.POST.get('confirm_user')
    password = request.POST.get('password')
    pass_data = json.loads(request.POST.get('pass_data', '{}'))
    user = auth_svc.login(email, pass_data, password)
    user_dict = None
    if user is not None:
        user_dict = _user2dict(user)
    if not confirm_user and user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
    return JsonResponse(user_dict, safe=False)


@csrf_exempt
def signup(request):
    email = request.POST['email']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    passimage_url = request.POST.get('passimage_url', '')
    password = request.POST.get('password', '')
    pass_data = json.loads(request.POST.get('pass_data', '{}'))
    auth_svc.signup(email, passimage_url, pass_data, first_name, last_name, password)
    return JsonResponse({})


@ajax_login_required
def logout(request):
    if request.method.lower() != 'post':
        raise Exception('Logout only via post')
    if request.user.is_authenticated:
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
def save_user(request):
    user_new_info = request.POST.dict()
    if 'pass_data' in user_new_info:
        user_new_info['pass_data'] = json.loads(user_new_info['pass_data'])
    user = request.user
    updated_credential = auth_svc.save_user(user_new_info, user)
    return JsonResponse({'user': updated_credential})


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


def get_passimage_url(request):
    params = request.GET.dict()
    passimage_url = passimage_svc.get_passimage_url(**params)
    return JsonResponse({'image_url': passimage_url})


@ajax_login_required
def list_logs(request):
    logs = log_svc.list_logs(request.user)
    return JsonResponse({'logs': logs})


def _user2dict(user):
    d = {
        'id': user.id,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'passimage_url': user.passimage_url
    }
    return d
