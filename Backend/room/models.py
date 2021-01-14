from django.db import models


class room(models.Model):
    id               = models.AutoField(primary_key=True)
    number           = models.CharField(max_length=50, null=False, blank=False)
    capacity         = models.CharField(max_length=50, null=False, blank=False)
    type             = models.CharField(max_length=50, null=False, blank=False)
    fees             = models.BooleanField(default = True)



    def __str__(self):
        return self.number

    class Meta():
        verbose_name = 'room'
        verbose_name_plural = 'rooms'
