from django.db import models
from room.models import room


class service(models.Model):
    id               = models.AutoField(primary_key=True)
    serviceName      = models.CharField(max_length=50, null=False, blank=False)
    description      = models.TextField()
    fees             = models.CharField(max_length=50, null=False, blank=False)
    type             = models.CharField(max_length=50, null=False, blank=False)
    image            = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.serviceName

    class Meta():
        verbose_name = 'service'
        verbose_name_plural = 'services'
