from django.contrib import admin
from django.urls import path
from veggie_restaurant import views as veggie_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', veggie_views.home, name='home'),  # Home page
    path('menu/', veggie_views.menu, name='menu'),  # Menu page
    path('booking/', veggie_views.booking, name='booking'),  # Booking page
]
