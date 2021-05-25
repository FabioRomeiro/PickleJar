from core.models import User
from core.service.auth_svc import encrypt_coords


def create_user(email='arthur@westmail.com', coords=((0.4, 0.4), (0.6, 0.6), (0.8, 0.8), (1.0, 1.0), (0.4, 0.4))):
    return User.objects.create(email=email, passcoord=encrypt_coords(coords))
