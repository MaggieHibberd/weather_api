from django.test import TestCase, Client
from django.urls import reverse
import json
import weather.views


class TestPage(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather/weather.html')
        self.assertContains(response, "What's the weather like?")


