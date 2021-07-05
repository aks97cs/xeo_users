# User_test
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class UserTest(APITestCase):
    fixtures = ['service/fixture/users.json']

    def test_user_count(self):
        """
        Ensure the user count in db is correct
        """
        user_count = 2
        self.assertEqual(user_count, User.objects.all().count())

    def test_user_create(self):
        """
        Ensure the user api post request is working
        """
        auth_url = reverse('user_auth')
        data = {"username": "shivam", "password": 12345}
        response = self.client.post(auth_url, data, format='json')

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.json().get('token', False))
        url = reverse('user_api')
        # check for duplicate user
        response = client.post(url, format='json', data={'username': 'shivam', 'password': 12345})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # check for weak validation
        response = client.post(url, format='json', data={'username': 'shivam', 'password': 123})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # check for valid data
        response = client.post(url, format='json', data={'username': 'admin1', 'password': 12345})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(3, User.objects.all().count())
        self.assertEqual('admin1', User.objects.get(username='admin1').username)

    def test_user_update(self):
        """
        Ensure the user update is working
        """
        auth_url = reverse('user_auth')
        data = {"username": "shivam", "password": 12345}
        response = self.client.post(auth_url, data, format='json')
        url = reverse('user_api_args', kwargs={'id': 10})
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.json().get('token', False))
        client.put(url, format='json', data={'username': 'shivoham', 'password': 12345})
        self.assertEqual('shivoham', User.objects.get(pk=10).username)








