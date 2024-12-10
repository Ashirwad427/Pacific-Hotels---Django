from django.contrib import admin
from .models import Booking, Contact

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'room_type', 'number_of_rooms', 'number_of_guests', 'visiting_dates')
    search_fields = ('name', 'email', 'room_type')  # Add a search box for these fields
    list_filter = ('room_type',)  # Add a filter for room type

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)