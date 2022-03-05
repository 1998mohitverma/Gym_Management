from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=40)
    date = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=70)
    price = models.CharField(max_length=40)
    unit = models.CharField(max_length=30)
    date = models.CharField(max_length=40)
    cname = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Plan(models.Model):
    name = models.CharField(max_length=70)
    amount = models.CharField(max_length=40)
    duration = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=70) 
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    plan = models.CharField(max_length=60)
    photo = models.ImageField(upload_to="myimages")
    joindate = models.CharField(max_length=40)
    expiredate = models.CharField(max_length=40)
    initialamount = models.CharField(max_length=10)
 
    def __str__(self):
        return self.name