from core.models import User


def create_user():
    return User.objects.create_user(
        username='arthur_morgan',
        first_name='Arthur',
        last_name='Morgan',
        email='arthur@westmail.com',
        password='lenny',
    )