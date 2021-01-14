from django.db import models
from room.models import room
from members.models import Users

class conductedFees(models.Model):
    user                 = models.ForeignKey(Users, on_delete=models.CASCADE)
    room                 = models.CharField(max_length=50, null=False, blank=False)
    totalFees            = models.CharField(max_length=50, null=False, blank=False, default='0')
    adminFees            = models.CharField(max_length=50, null=False, blank=False, default='0')





    def __str__(self):
        return self.totalFees

    class Meta():
        verbose_name = 'conductedFees'
        verbose_name_plural = 'conductedFeess'
