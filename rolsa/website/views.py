from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'webpages/home.html')

def carbonFootprintCalculator(request):
    return render(request, 'webpages/carbon-footprint-calculator.html')