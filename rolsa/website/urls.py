from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('carbon-footprint-calculator/', views.carbonFootprintCalculator, name="carbonFootprintCalculator")
]