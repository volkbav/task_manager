from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

# Create your tests here.

# интеграционный тест
class UserTest(TestCase):
    # проверяем ответ от приложения users

    def setUp(self):
        self.user = User.objects.create(
            username="john",
        first_name="John",
        email="john@example.com",
        password="123456")
    
    def test_user_list(self):
        response = self.client.get(reverse("users:users"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John")