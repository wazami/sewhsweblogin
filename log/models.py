from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100) #this can have a function in which you authenticate

class Club(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, related_name="owned_clubs")
    members = models.ManyToManyField(User, blank=True)

