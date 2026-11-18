from django.test import TestCase
from accounts.models import CustomUser


class CustomUserModelTests(TestCase):
    def test_default_role_is_commuter(self):
        user = CustomUser.objects.create_user(
            username='u1', email='u1@example.com', password='pass12345'
        )
        self.assertEqual(user.role, CustomUser.Role.COMMUTER)

    def test_str_contains_username(self):
        user = CustomUser.objects.create_user(
            username='u1', email='u1@example.com', password='pass12345'
        )
        self.assertIn('u1', str(user))