import email
from django.db import models

# Create your models here.
class Data(models.Model):
    id=models.AutoField
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    city=models.CharField(max_length=15)
    email=models.CharField(max_length=25)
    state=models.CharField(max_length=15)
    zip=models.IntegerField(max_length=6)
    def __str__(self) :
        return  self.first_name
