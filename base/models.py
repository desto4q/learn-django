from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    name= models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Room(models.Model):
    # host
    Topic = models.ForeignKey(Topic,on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participant = models
    updated = models.DateTimeField(auto_now=True)
    creared = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
class message(models.Model):
    # user
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField(null=False,blank=False)
    updated = models.DateTimeField(auto_now=True)
    creared = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body[50]