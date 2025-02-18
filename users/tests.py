from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status

class UserRegistrationTest(APITestCase):
    def test_register_user(self):
        data = {
            "email": "testuser@example.com",
            "username": "testuser",
            "password": "testpassword"
        }
        response = self.client.post('/users/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
