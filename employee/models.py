from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class employee_model(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=(50))
    address = models.TextField()
    designation = models.CharField(max_length=(255))

    def __str__(self):
        return self.name
