from django.urls import path
from core.consumers import CredentialsConsumer


ws_urlpatterns = [
    path('ws/credentials/', CredentialsConsumer.as_asgi())
]
