from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import carbonFootprint

# Create your views here.
def home(request):
    return render(request, 'webpages/home.html')

def carbonFootprintCalculator(request):
    # If get has the query params containing the data then we can save it
    if request.GET.get("calculatedSum"):
        try:
            if (float(request.GET.get("calculatedSum")) < 0):
                raise ValueError("Carbon footprint cannot be negative")
        except ValueError:
            return render(request, 'webpages/carbon-footprint-calculator.html')
        if request.user.is_authenticated:
            # overwrite if exists, else create new
            if carbonFootprint.objects.filter(footprintUserID=request.user).exists():
                carbonFootprint.objects.filter(footprintUserID=request.user).update(
                    carbonFootprint=request.GET.get("calculatedSum"),
                )
            else:
                carbonFootprint.objects.create(
                    footprintUserID=request.user,
                    carbonFootprint=request.GET.get("calculatedSum"),
                )


    # If the params are not set and the user is logged in and they have a reading add their current reading to their params
    if request.user.is_authenticated:
        if carbonFootprint.objects.filter(footprintUserID=request.user).exists():
            currentReading = carbonFootprint.objects.get(footprintUserID=request.user)
            return render(request, 'webpages/carbon-footprint-calculator.html', {"previousReading": currentReading.carbonFootprint})
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