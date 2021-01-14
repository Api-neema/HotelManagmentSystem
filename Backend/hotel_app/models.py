from django.db import models


class hotel(models.Model):
    hotelName           = models.CharField(max_length=50, null=False, blank=False)
    hotelAddress        = models.CharField(max_length=50, null=False, blank=False)
    singleRooms         = models.CharField(max_length=50, null=False, blank=False)
    doubleRooms         = models.CharField(max_length=50, null=False, blank=False)
    tripleRooms         = models.CharField(max_length=50, null=False, blank=False)



    def __str__(self):
        return self.hotelName

    class Meta():
        verbose_name = ' hotel'
        verbose_name_plural = ' hotels'
