from django.db import models
from members.models import Users


class query(models.Model):
    query                    = models.TextField()
    email                    = models.CharField(max_length=50, null=False, blank=False)
    userName                 = models.CharField(max_length=50, null=False, blank=False)
    user                     = models.ForeignKey(Users ,on_delete=models.CASCADE, null=True)





    def __str__(self):
        return self.email

    class Meta():
        verbose_name = 'query'
        verbose_name_plural = 'querys'
