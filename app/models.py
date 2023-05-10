from django.db import models

# Create your models here.

class Student(models.Model):
    Sname=models.CharField(max_length=100)
    Sage=models.IntegerField()
    Saddress=models.TextField()
    Smail=models.EmailField(default=0)
    Surl=models.URLField(default=0)