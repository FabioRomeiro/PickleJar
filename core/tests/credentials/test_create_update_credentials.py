from django.test.client import Client
from django.test.testcases import TestCase
from model_bakery import baker

from core.models import Credential
from core.tests.fixtures import users


class TestCreateUpdateCredentials(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = users.create_user()
        cls.credential_whatsapp = baker.make(Credential, name='Whatsapp', owner=cls.user)

    def setUp(self):
        self.client = Client()
        self.client.force_login(self.user)
    
    def test_create_credential(self):
        expected_credential = {
            'name': 'Facebook',
            'username': 'arthur_morgan@westmail.com',
            'password': 'lenny',
            'link': 'https://facebook.com'
        }
        response = self.client.post('/api/credentials/save', expected_credential)
        self.assertEqual(response.status_code, 200)
        credential = Credential.objects.get(username=expected_credential['username'])
        credential_dict = credential.to_dict_json()
        self.assertEqual(credential_dict['name'], expected_credential['name'])
        self.assertEqual(credential_dict['username'], expected_credential['username'])
        self.assertIn('created_at', credential_dict)
        self.assertIn('last_updated', credential_dict)
        self.assertIn('last_accessed', credential_dict)

    def test_save_credential(self):
        expected_credential = self.credential_whatsapp.to_dict_json()
        expected_credential.update({
            'name': 'Whatsapp 2'
        })
        response = self.client.post('/api/credentials/save', expected_credential)
        self.assertEqual(response.status_code, 200)
        credential = Credential.objects.get(pk=self.credential_whatsapp.pk)
        self.assertEqual(credential.name, expected_credential['name'])

    def test_delete_credential(self):
        response = self.client.post('/api/credentials/delete', {'id': self.credential_whatsapp.pk})
        self.assertEqual(response.status_code, 200)
        credential = Credential.objects.filter(pk=self.credential_whatsapp.pk)
        self.assertFalse(credential.exists())

