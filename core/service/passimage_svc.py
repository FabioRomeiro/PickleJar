from core.models import User


def get_passimage_url(user_email):
    return User.objects.get(email=user_email).passimage_url
