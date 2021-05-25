from core.models import User
from django.test.client import Client
from django.test.testcases import TestCase
import json

from core.tests.fixtures import users


class TestAuth(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.arthur = users.create_user()

    def setUp(self):
        self.client = Client()

    def test_whoami(self):
        response = self.client.get('/api/whoami')
        self.assertEqual(200, response.status_code)

    def test_login(self):
        response = self.client.post('/api/login', {
            'email': 'arthur@westmail.com',
            'pass_data': json.dumps({
                'grid_size': 500,
                'coords': [
                    {'x': 224, 'y': 211}, {'x': 325, 'y': 322}, {'x': 422, 'y': 383},
                    {'x': 500, 'y': 500}, {'x': 203, 'y': 225}
                ]
            })
        })
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            'id': self.arthur.id,
            'email': self.arthur.email
        })

    def test_signup(self):
        response = self.client.post('/api/signup', {
            'email': 'lenny@westmail.com',
            'pass_data': json.dumps({
                'grid_size': 500,
                'coords': [
                    {'x': 465, 'y': 231}, {'x': 53, 'y': 263}, {'x': 196, 'y': 130},
                    {'x': 13, 'y': 151}, {'x': 176, 'y': 273}
                ]
            })
        })
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {})


    #
    # def test_auth_api(self):
    #     client.force_login(User.objects.get(username='jon'))
    #     r3 = client.get('/api/whoami')
    #     r4 = client.post('/api/logout')
    #     r5 = client.get('/api/whoami')
