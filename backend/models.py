from django.contrib.gis.db import models
from django.utils.crypto import get_random_string


class Culture(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


def generate_unique_key():
    return get_random_string(length=15)


class Farmer(models.Model):
    unique_key = models.CharField(default=generate_unique_key, unique=True, max_length=15)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name


class Plot(models.Model):
    contour = models.PointField()
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    SEASONS_CHOICES = (
        ('весна', 'весна'),
        ('лето', 'лето'),
        ('осень', 'осень'),
        ('зима', 'зима'),
    )
    season = models.CharField(max_length=10, choices=SEASONS_CHOICES, default='весна')
