from django.db import models

# Create your models here.

class Bars(models.Model):
    bar_id = models.AutoField(primary_key=True)
    bar_name = models.CharField(max_length=500)

class Beers(models.Model):
    beer_id = models.AutoField(primary_key=True)
    beer_name = models.CharField(max_length=500)
    bar = models.CharField(max_length=500)
    dateofcreation = models.DateField()
    photo = models.CharField(max_length=500)