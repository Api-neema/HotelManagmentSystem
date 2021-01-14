from django.db import models
from room.models import room

class Payment(models.Model):
    id                = models.AutoField(primary_key=True)
    cardType          = models.CharField(max_length=50, null=False, blank=False)
    cardNumber        = models.CharField(max_length=50, null=False, blank=False)
    expiryDate        = models.CharField(max_length=50, null=False, blank=False)


    def __str__(self):
        return self.cardNumber

    class Meta():
        verbose_name = 'creditCard'
        verbose_name_plural = 'creditCards'
