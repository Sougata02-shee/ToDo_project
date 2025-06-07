from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class TaskModel(models.Model):
    Title=models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    Due_date=models.CharField(default=date.today)
    priority=models.IntegerField(default=0)
    Status=models.CharField(default='incomplete')