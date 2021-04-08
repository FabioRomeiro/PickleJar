from django.test.client import Client
from django.test.testcases import TestCase


class TestCreateUpdateCredentials(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        self.client = Client()
    
    def test_create_credential(self):
        pass

    def test_save_credential(self):
        pass

    def test_delete_credential(self):
        pass
