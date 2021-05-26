from django.db import models
import datetime
# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=100)
    uniqueID = models.CharField(max_length=100)
    dob =  models.DateField(null=True)

    def __str__(self):
        return self.username