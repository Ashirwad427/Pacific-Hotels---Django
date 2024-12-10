from django.shortcuts import render, HttpResponse
from .models import Booking, Contact
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')

@login_required
def explore(request):
    return render(request,'explore.html')

@login_required
def rooms(request):
    return render(request,'rooms.html')

@login_required
def booking(request):
    return render(request,'bb.html')


@login_required
@csrf_exempt
def handle_form(request):
    if request.method == 'POST':
        # Extract form data from the request
        name = request.POST.get('name')
        email = request.POST.get('email')
        room_type = request.POST.get('Rooms')
        number_of_rooms = request.POST.get('number1')
        number_of_guests = request.POST.get('number2')
        arrival_date = request.POST.get('arrival_date')
        departure_date = request.POST.get('departure_date')

        # Combine arrival and departure dates
        visiting_dates = f"{arrival_date} to {departure_date}"

        # Save to the Booking model
        booking = Booking(
            name=name,
            email=email,
            room_type=room_type,
            number_of_rooms=number_of_rooms,
            number_of_guests=number_of_guests,
            visiting_dates=visiting_dates,
            user=request.user  # Link to the logged-in user
        )
        booking.save()

    return render(request, 'bb.html')


@login_required
def newpage(request):
    bookings = Booking.objects.filter(user=request.user)  # Filter by logged-in user
    return render(request, 'new.html', {'bookings': bookings})


@login_required
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        # Save to database
        Contact.objects.create(name=name, email=email, message=message)
        # Render the Thank You page
        return render(request, "thank_you.html")

    return render(request, "contact.html")