from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')

def booking(request):
    return render(request, 'booking.html')