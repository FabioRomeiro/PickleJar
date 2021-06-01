from django.urls import path
from core.consumers import CredentialsConsumer, UserConsumer

ws_urlpatterns = [
    path('ws/credentials/', CredentialsConsumer.as_asgi()),
    path('ws/user/', UserConsumer.as_asgi())
]
