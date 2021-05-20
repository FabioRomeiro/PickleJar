from core import views
from django.urls import path

urlpatterns = [
    path('api/dapau', views.dapau),
    path('api/login', views.login),
    path('api/logout', views.logout),
    path('api/whoami', views.whoami),

    # Credential
    path('api/credentials/save', views.save_credential),
    path('api/credentials/delete', views.delete_credential),
    path('api/credentials/password', views.get_password),
    path('api/credentials', views.list_credentials),

    # Logs
    path('api/logs', views.list_logs),
]
