from django.test import TestCase
from myblog.models import Client
class ClientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Client.objects.create(first_name='Pasha', last_name='Technik')



