from dataclasses import field
from django.db import models

class mainpageinfo(models.Model):
    symptm1=models.CharField(max_length=200)
    symptm2=models.CharField(max_length=200)
    symptm3=models.CharField(max_length=200)
    symptm4=models.CharField(max_length=200)
    symptm5=models.CharField(max_length=200)
    Disease=models.CharField(max_length=200,null=True)
    date_time=models.CharField(max_length=200,null=True)
    class Meta:
        db_table="mainpageinfo"

class feedback(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email_adrs=models.EmailField(max_length=200)
    suggestions=models.CharField(max_length=200)
    date_time=models.CharField(max_length=200,null=True)
    class Meta:
        db_table="feedback"

    
    