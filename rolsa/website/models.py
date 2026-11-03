from django.db import models
from django.conf import settings

# Create your models here.
class installation(models.Model): 
    PRODUCTS=[  
        ('P1', 'Solar Panels'),
        ('P2', 'EV Charging'),
        ('P3', 'EV Car'),
        ('P4', 'Solar Batteries'),
        ('P5', 'Wind Farm'),
    ]
    STATUSES=[  
        ('Prog', 'In-progress'),
        ('Canc', 'Cancelled'),
        ('Comp', 'Completed'),
        ('Pend', 'Pending'),
    ]
    installUserID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="install_bookings")
    installDate = models.DateTimeField()
    productType = models.CharField(choices=PRODUCTS)
    status = models.CharField(choices=STATUSES, default="Pend") 


class consultation(models.Model): 
    STATUSES=[
        ('Done', 'Done'),
        ('Canc', 'Cancelled'),
        ('Pend', 'Pending'),
        ('Prog', 'In-progress'),
    ]
    consultUserID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="consult_bookings")
    consultDate = models.DateTimeField()
    consultType = models.CharField(max_length=100)
    status = models.CharField(choices=STATUSES, default="Pend") 


class usage(models.Model): 
    usageUserID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="usage")
    logDate = models.DateTimeField(auto_now_add=True)
    kwhConsumed = models.FloatField(default=0)

class carbonFootprint(models.Model):
    footprintUserID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="carbonfootprint")
    carbonFootprint = models.FloatField(default=0)