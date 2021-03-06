from django.db import models
from django.core.validators import int_list_validator

# Create your models here.

class Fenster(models.Model):
    fenster_width = models.IntegerField(default=50)
    fenster_height = models.IntegerField(default=50)
    fenster_scheme = models.CharField(
        validators=[int_list_validator],
        default='1,2',
        max_length=1024
    )
    fenster_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=1
    )
    for_rent = models.BooleanField(default=True)
    window_view = models.CharField(default='', max_length=1024)

class Apt(models.Model):
    fenster = models.ForeignKey(Fenster, on_delete=models.CASCADE)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    altitude = models.FloatField(null=False)

