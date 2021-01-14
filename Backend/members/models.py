from django.db import models
from service.models import service
from payment.models import Payment

class Users(models.Model):
    id                   = models.AutoField(primary_key=True)
    firstName            = models.CharField(max_length=50, null=False, blank=False)
    lastName             = models.CharField(max_length=50, null=False, blank=False)
    password             = models.CharField(max_length=50, null=False, blank=False)
    mobileNumber         = models.CharField(max_length=50, null=True, blank=False)
    gender               = models.CharField(max_length=50, null=True, blank=False)
    email                = models.EmailField(max_length=50, null=False, blank=False)
    dateOfBirth          = models.CharField(max_length=50, null=True, blank=False)
    type                 = models.CharField(max_length=50, null=False, blank=False)
    service              = models.ManyToManyField(service, null=True)
    card                 = models.ForeignKey(Payment ,on_delete=models.CASCADE, null=True)



    def __str__(self):
        return self.email

    class Meta():
        verbose_name = 'user'
        verbose_name_plural = 'users'
