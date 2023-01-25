from django.db import models

# Create your models here.
# create table for registration

class regmodel(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class employeemodel(models.Model):
    name = models.CharField(max_length=25)
    salary= models.IntegerField()
    email= models.EmailField()
    cname= models.CharField(max_length=20)
    dname= models.CharField(max_length=20)
    def __str__(self):
        return self.name


class filemodel(models.Model):
    itemname=models.CharField(max_length=20)
    image=models.FileField(upload_to='newapp/static')
    def __str__(self):
        return self.itemname


class cardmodel(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    image=models.FileField(upload_to='newapp/static')
    description=models.CharField(max_length=60)
    def __str__(self):
        return self.name


class xammodel(models.Model):
    name=models.CharField(max_length=20)
    image=models.FileField(upload_to='newapp/static')


