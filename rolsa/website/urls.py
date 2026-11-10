from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name=""),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path('carbon-footprint-calculator/', views.carbonFootprintCalculator, name="carbonFootprintCalculator"),
    path("book-installation/", views.installationBooking, name="installationBooking"),
    path("book-consultation/", views.consultationBooking, name="consultationBooking"),
]