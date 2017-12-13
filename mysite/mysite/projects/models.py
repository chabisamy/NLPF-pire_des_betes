from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)


class CounterPart(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=3, max_digits=10)
