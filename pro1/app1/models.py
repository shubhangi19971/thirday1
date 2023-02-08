from django.db import models

class Person(models.Model):
    pid = models.IntegerField()
    name = models.CharField(max_length=90)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
