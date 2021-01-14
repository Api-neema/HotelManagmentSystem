from django.db import models


class feedback(models.Model):
    feedback                 = models.TextField()
    email                    = models.CharField(max_length=50, null=False, blank=False)
    userName                 = models.CharField(max_length=50, null=False, blank=False)






    def __str__(self):
        return self.email

    class Meta():
        verbose_name = 'feedback'
        verbose_name_plural = 'feedbacks'
