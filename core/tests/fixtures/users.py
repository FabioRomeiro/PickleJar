from core.models import User


def create_user(username='arthur_morgan', first_name='Arthur', last_name='Morgan', email='arthur@westmail.com',
                password='lenny'):
    return User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                    password=password)