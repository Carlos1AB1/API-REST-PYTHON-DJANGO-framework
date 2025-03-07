from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    is_student = models.BooleanField(default=False)
