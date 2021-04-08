from django.test.client import Client
from django.test.testcases import TestCase


class TestListCredentials(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        self.client = Client()
    
    def test_list_credentials(self):
        pass

    def test_list_favorite_credentials(self):
        pass

    def test_list_credentials_by_text(self):
        pass

    def test_list_recent_accessed_credentials(self):
        pass

    def test_get_number_of_credentials(self):
        pass

    def test_get_number_of_credentials(self):
        pass
