from django.test.client import Client
from django.test.testcases import TestCase
from model_bakery import baker

from core.models import Credential
from core.tests.fixtures import users


class TestListCredentials(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = users.create_user()
        cls.credential_whatsapp = baker.make(Credential, name='Whatsapp 2', favorite=True, owner=cls.user)
        cls.credential_facebook = baker.make(Credential, name='Facebook', owner=cls.user)

    def setUp(self):
        self.client = Client()
        self.client.force_login(self.user)
    
    def test_list_credentials(self):
        response = self.client.get('/api/credentials')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('credentials', data)
        expected_credentials = [
            self.credential_facebook.to_dict_json(),
            self.credential_whatsapp.to_dict_json()
        ]
        self.assertEqual(data['credentials'], expected_credentials)

    def test_list_favorite_credentials(self):
        response = self.client.get('/api/credentials', {'favorite_only': True})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('credentials', data)
        self.assertEqual(data['credentials'], [self.credential_whatsapp.to_dict_json()])

    def test_list_credentials_by_text(self):
        response = self.client.get('/api/credentials', {'search_text': 'Fa'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('credentials', data)
        self.assertEqual(data['credentials'], [self.credential_facebook.to_dict_json()])

    def test_list_recent_accessed_credentials(self):
        response = self.client.get('/api/credentials', {'order_by': '-last_accessed'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        expected_credentials = [
            self.credential_facebook.to_dict_json(),
            self.credential_whatsapp.to_dict_json()
        ]
        self.assertIn('credentials', data)
        self.assertEqual(data['credentials'], expected_credentials)

    def test_get_number_of_credentials(self):
        response = self.client.get('/api/credentials', {'count_only': True})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('count_credentials', data)
        self.assertEqual(data['count_credentials'], 2)
