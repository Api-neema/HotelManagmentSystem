from django.db import models
from hotel_app.models import hotel
from members.models import Users
from service.models import service
class booking(models.Model):
    id                    = models.AutoField(primary_key=True)
    user                  = models.ForeignKey(Users, on_delete=models.CASCADE)
    hotelName             = models.CharField(max_length=50, null=True, blank=False)
    roomCapacity          = models.CharField(max_length=50, null=True, blank=False)
    roomNumber            = models.CharField(max_length=50, null=True, blank=False)
    roomType              = models.CharField(max_length=50, null=True, blank=False)
    startDate             = models.CharField(max_length=50, null=True, blank=False)
    endDate               = models.CharField(max_length=50, null=True, blank=False)
    checkIn               = models.BooleanField(default = True,null=True)
    service               = models.ForeignKey(service, on_delete=models.CASCADE , null=True)
    bookingType           = models.BooleanField(default=True) 
    accepted              = models.BooleanField(null=True) 

    def __str__(self):
        return self.roomNumber  

    class Meta():
        verbose_name = 'Booking'
        verbose_name_plural = 'bookings'
