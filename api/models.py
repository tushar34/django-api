from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.conf import settings

# Create your models here.


# class User(AbstractUser):
#     email = models.CharField(max_length=20, unique=True)
#     username = None
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []


class Board(models.Model):
    board_name = models.CharField(max_length=15,unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class List(models.Model):
    list_name = models.CharField(max_length=15,unique=True,null=False,blank=False)
    list_order = models.IntegerField()
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)


class Card(models.Model):
    card_name = models.CharField(max_length=15,unique=True)
    description = models.CharField(max_length=15,null=True,blank=True)
    card_order = models.IntegerField()
    image=models.ImageField(upload_to='media/',blank=True,null=True)
    list_id = models.ForeignKey(List, on_delete=models.CASCADE)
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
