from django.contrib import admin
from django.urls import path
from veggie_restaurant import views as veggie_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', veggie_views.home, name='home'),  # Home page
    path('menu/', veggie_views.menu, name='menu'),  # Menu page
    path('booking/', veggie_views.booking, name='booking'),  # Booking page
     path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), # Log in page
    path('signup/', veggie_views.signup, name='signup'), # Sign up page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # Logout page
]
