# login/tests/test_views.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginViewTest(TestCase):
    def setUp(self):
        self.login_url = reverse('login:login')
        self.home_url = reverse('home:index')
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_login_with_valid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertRedirects(response, self.home_url)  # Check for redirection to home

    def test_login_with_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'wronguser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  # Page reloads with error
        self.assertContains(response, "Invalid username or password.")  # Check for error message

    def test_login_when_already_authenticated(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.login_url)
        self.assertRedirects(response, self.home_url)

class LogoutViewTest(TestCase):
    def setUp(self):
        self.logout_url = reverse('login:logout')
        self.login_url = reverse('login:login')
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_logout_user(self):
        self.client.login(username='testuser', password='password123')  # Log in first
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, self.login_url)  # Check redirection to login
        response = self.client.get(self.logout_url)
        self.assertFalse('_auth_user_id' in self.client.session)  # Check session cleared

class RegisterViewTest(TestCase):
    def setUp(self):
        self.register_url = reverse('login:register')
        self.home_url = reverse('home:index')

    def test_register_with_valid_data(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123'
        })
        self.assertRedirects(response, self.home_url)  # Check redirection to home
        self.assertTrue(User.objects.filter(username='newuser').exists())  # User created

    def test_register_with_invalid_data(self):
        response = self.client.post(self.register_url, {
            'username': '',
            'password1': 'password',
            'password2': 'password'
        })
        self.assertEqual(response.status_code, 200)  # Page reloads
        self.assertContains(response, "This field is required.")  # Check error message
        self.assertFalse(User.objects.filter(username='').exists())  # User not created

    def test_register_with_mismatched_passwords(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'password1': 'password123',
            'password2': 'differentpassword'
        })
        self.assertEqual(response.status_code, 200)  # Page reloads
        self.assertContains(response, "The two password fields didn’t match.")  # Check error

    def test_register_with_common_password(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'password1': 'password123',  # Common password
            'password2': 'password123'
        })
        self.assertEqual(response.status_code, 200)  # Page reloads
        self.assertContains(response, "This password is too common.")  # Check error
        self.assertFalse(User.objects.filter(username='newuser').exists())  # User not created

    def test_register_with_entirely_numeric_password(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'password1': '12345678',  # Entirely numeric password
            'password2': '12345678'
        })
        self.assertEqual(response.status_code, 200)  # Page reloads
        self.assertContains(response, "This password is entirely numeric.")  # Check error
        self.assertFalse(User.objects.filter(username='newuser').exists())  # User not created

    def test_register_with_password_similar_to_username(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'password1': 'newuser123',  # Password similar to username
            'password2': 'newuser123'
        })
        self.assertEqual(response.status_code, 200)  # Page reloads
        self.assertContains(response, "The password is too similar to the username.")  # Check error
        self.assertFalse(User.objects.filter(username='newuser').exists())  # User not created

    def test_register_with_short_password(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'password1': '12345',  # Short password
            'password2': '12345'
        })
        self.assertEqual(response.status_code, 200)  # Page reloads
        self.assertContains(response, "This password is too short.")  # Check error
        self.assertFalse(User.objects.filter(username='newuser').exists())  # User not created