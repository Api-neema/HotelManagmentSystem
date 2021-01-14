from django.db import models


class review(models.Model):
    description                 = models.TextField()
    rating                      = models.CharField(max_length=10, null=False, blank=False)
    userName                    = models.CharField(max_length=50, null=False, blank=False)






    def __str__(self):
        return self.rating

    class Meta():
        verbose_name = 'review'
        verbose_name_plural = 'reviews'
