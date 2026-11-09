from django.shortcuts import render, redirect
from .forms import RegistrationForm

# Create your views here.
def home(request):
    return render(request, 'webpages/home.html')

def carbonFootprintCalculator(request):
    return render(request, 'webpages/carbon-footprint-calculator.html')

def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegistrationForm()
    return render(request, "registration/register.html", {"form": form})