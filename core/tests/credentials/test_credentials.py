from django.test.testcases import TestCase
from model_bakery import baker

from core.models import Credential
from core.tests.fixtures import users


class TestCredentials(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = users.create_user()
        cls.credential_whatsapp = baker.make(Credential, name='Whatsapp 2', favorite=True, owner=cls.user)

    def test_show_model_as_string(self):
        self.assertEqual(str(self.credential_whatsapp), self.credential_whatsapp.name)

    def test_show_model_as_dict_json(self):
        whatsapp_dict = self.credential_whatsapp.to_dict_json()
        self.assertEqual(whatsapp_dict, {
            'id': self.credential_whatsapp.id,
            'name': self.credential_whatsapp.name,
            'username': self.credential_whatsapp.username,
            'image': self.credential_whatsapp.image,
            'link': self.credential_whatsapp.link,
            'notes': self.credential_whatsapp.notes,
            'favorite': self.credential_whatsapp.favorite,
            'status': str(self.credential_whatsapp.status),
            'created_at': str(self.credential_whatsapp.created_at),
            'last_updated': str(self.credential_whatsapp.last_updated),
            'last_accessed': str(self.credential_whatsapp.last_accessed)
        })
