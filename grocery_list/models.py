from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category (models.Model):
    name = models.CharField()


class Product (models.Model):
    name = models.CharField()
    brand = models.CharField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)





