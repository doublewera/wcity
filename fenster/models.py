from django.db import models

# Create your models here.

class Fenster(models.Model):
    fenster_width = models.IntegerField()
    window_view = models.CharField(default='', max_length=1024)

class Apt(models.Model):
    fenster = models.ForeignKey(Fenster, on_delete=models.CASCADE)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    altitude = models.FloatField(null=False)

