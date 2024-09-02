from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Booking

def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')

@login_required
def booking(request):
    user_bookings = Booking.objects.filter(user=request.user).order_by('-date', '-time')

    if request.method == 'POST':
        # Capture form data
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        date = request.POST['date']
        time = request.POST['time']
        number_of_guests = request.POST['number_of_guests']
        special_requests = request.POST.get('special_requests', '')

        # Create and save the new booking
        new_booking = Booking.objects.create(
            user=request.user,
            name=name,
            email=email,
            phone_number=phone_number,
            date=date,
            time=time,
            number_of_guests=number_of_guests,
            special_requests=special_requests
        )

        return redirect('booking')

    return render(request, 'booking.html', {'user_bookings': user_bookings})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})