from django.test.testcases import TestCase
from model_bakery import baker

from core.models import PassImage
from core.service import passimage_svc
from core.tests.fixtures import users


class Testpassimage(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_arthur = users.create_user()
        cls.passimage_arthur = baker.make(PassImage, user=cls.user_arthur, image_url='https://picsum.photos/500/500')

    def test_show_model_as_string(self):
        self.assertEqual(str(self.passimage_arthur), self.passimage_arthur.image_url)

    def test_show_model_as_dict_json(self):
        whatsapp_dict = self.passimage_arthur.to_dict_json()
        self.assertEqual(whatsapp_dict, {
            'user_email': self.user_arthur.email,
            'image_url': self.passimage_arthur.image_url
        })

    def test_get_passimage_url(self):
        response = self.client.get('/api/passimage', {'user_email': self.user_arthur.email})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('image_url', data)
        self.assertEqual(data['image_url'], self.passimage_arthur.image_url)

    def test_save_passimage(self):
        new_image_url = 'https://picsum.photos/400/400'
        passimage_svc.save_passimage(self.user_arthur, new_image_url)
        arthur_passimage = PassImage.objects.get(user__email=self.user_arthur.email)
        self.assertEqual(arthur_passimage.image_url, new_image_url)
        self.assertEqual(self.user_arthur.email, arthur_passimage.user.email)
