from django.test import TestCase
from django.urls import reverse

# Create your tests here.

# интеграционный тест
class UserTest(TestCase):
    # проверяем ответ от приложения users
    def test_user_list(self):
        response = self.client.get(reverse("users:users"))
        self.assertEqual(response.status_code, 200)