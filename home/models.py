from django.db import models
from django.contrib.auth.models import User  # Import User model

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    room_type = models.CharField(max_length=50)
    number_of_rooms = models.IntegerField()
    number_of_guests = models.IntegerField()
    visiting_dates = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add user reference

    def __str__(self):
        return f"{self.name} - {self.room_type}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
