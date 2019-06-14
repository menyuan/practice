from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    age  = models.IntegerField(default=18)
    sex  = models.CharField(max_length=2)
    education = models.CharField(max_length=10)
    phone = models.CharField(max_length=11)
    major =models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    university = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    email =models.CharField(max_length=30,blank=True)
    def __str__(self):
        return self.name
