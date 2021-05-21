from core.models import PassImage


def get_passimage_url(user_email):
    return PassImage.objects.get(user__email=user_email).image_url


def save_passimage(user, new_image_url):
    PassImage.objects.filter(user=user).update(image_url=new_image_url)
