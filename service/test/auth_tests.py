# Auth_Test
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


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

    def test_api_authorization(self):
        """
        Ensure that api could not be access
        without auth
        """
        url = reverse('user_api')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        auth_url = reverse('user_auth')
        data = {"username": "shivam", "password": 12345}
        # request without auth token
        response = self.client.post(auth_url, data, format='json')

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.json().get('token', False))
        # check request with header auth
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
