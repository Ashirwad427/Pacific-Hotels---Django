from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from home.models import Booking, Contact

class ViewsTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()

        # Define URLs with the namespace 'home'
        self.index_url = reverse('home:index')
        self.explore_url = reverse('home:explore')
        self.rooms_url = reverse('home:rooms')
        self.booking_url = reverse('home:booking')
        self.handle_form_url = reverse('home:handle_form')
        self.newpage_url = reverse('home:my_bookings')
        self.contact_url = reverse('home:contact')

    def test_index_view_requires_login(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 302)  # Redirect to login

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)  # Successfully loads

    def test_explore_view_requires_login(self):
        response = self.client.get(self.explore_url)
        self.assertEqual(response.status_code, 302)

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.explore_url)
        self.assertEqual(response.status_code, 200)

    def test_rooms_view_requires_login(self):
        response = self.client.get(self.rooms_url)
        self.assertEqual(response.status_code, 302)

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.rooms_url)
        self.assertEqual(response.status_code, 200)

    def test_booking_view_requires_login(self):
        response = self.client.get(self.booking_url)
        self.assertEqual(response.status_code, 302)

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.booking_url)
        self.assertEqual(response.status_code, 200)

    def test_handle_form_creates_booking(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.handle_form_url, {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'Rooms': 'luxurys',
            'number1': 1,
            'number2': 2,
            'arrival_date': '2024-12-01',
            'departure_date': '2024-12-10',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Booking.objects.count(), 1)
        booking = Booking.objects.first()
        self.assertEqual(booking.name, 'Test User')
        self.assertEqual(booking.user, self.user)

    def test_newpage_shows_user_bookings(self):
        self.client.login(username='testuser', password='testpassword')
        Booking.objects.create(
            name='Test Booking',
            email='testuser@example.com',
            room_type='luxurys',
            number_of_rooms=1,
            number_of_guests=2,
            visiting_dates='2024-12-01 to 2024-12-10',
            user=self.user,
        )
        response = self.client.get(self.newpage_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Booking')

    def test_contact_view_saves_message(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.contact_url, {
            'name': 'Contact User',
            'email': 'contact@example.com',
            'message': 'This is a test message.',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Contact.objects.count(), 1)
        contact = Contact.objects.first()
        self.assertEqual(contact.name, 'Contact User')
        self.assertEqual(contact.email, 'contact@example.com')
