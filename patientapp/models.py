from django.db import models
from django import forms

import datetime
# Create your models here.

"""
class UserInfo(models.Model):
    username = models.CharField(max_length=100)
    uniqueID = models.CharField(max_length=100)
    dob =  models.DateField(null=True)
    document = models.FileField(upload_to='Files/')

    def __str__(self):
        return self.username
"""


class EmpInfo(models.Model):
    empname = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    mobile = models.IntegerField()
    email = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    resume = models.FileField(upload_to='Resumes/')
    resume_path = models.CharField(default="", max_length=100)

    def __str__(self):
        return self.empname
