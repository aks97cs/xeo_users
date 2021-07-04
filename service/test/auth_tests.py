# Auth_Test
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class AuthTest(APITestCase):
    fixtures = ['service/fixture/users.json']

    def test_user_auth(self):
        """
        Ensure if user credential is valid, this will return us the
        user authentication token
        """
        url = reverse('user_auth')
        data = {"username": "shivam", "password": 12345}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.json().get('token', False), False)
