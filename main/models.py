from django.db import models


# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    rating = models.IntegerField(default=0, blank=True, null=True)
    duration = models.FloatField(default=0)



    def __str__(self):
        return self.title
