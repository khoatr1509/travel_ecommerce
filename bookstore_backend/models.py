from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=128)
    author = models.CharField(max_length=50)
    quantity = models.IntegerField()
    description = models.TextField(default='no description')
    image = models.ImageField(
        default='images/default_book.png', upload_to='upload/')


class Tour(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(default='no description')
    image = models.ImageField(
        default='images/default_book.png', upload_to='upload/')
