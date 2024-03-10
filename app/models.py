# models.py
from django.db import models

class registerdetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
class taskshow(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    deadline=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)

