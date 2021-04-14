from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Owner(models.Model):
    oId = models.AutoField(primary_key=True)
    oFname = models.CharField(max_length=100)
    oLname = models.CharField(max_length=100)
    oEmail = models.EmailField(unique=True)
    oPassword = models.CharField(max_length=128)
    oMobile = models.BigIntegerField()
    oGender = models.CharField(max_length=4)
    oDOB = models.DateField()

    def __str__(self):
        return f'{self.oFname} {self.oLname}'


class Room(models.Model):
    rId = models.AutoField(primary_key=True)
    rOid = models.ForeignKey(Owner, on_delete=CASCADE)
    rPrice = models.IntegerField()
    rAddress = models.CharField(max_length=100)
    rCity = models.CharField(max_length=100)
    rState = models.CharField(max_length=100)
    rShare = models.IntegerField()
    rGirlsOnly = models.BooleanField(default=False)
    rBathroom = models.IntegerField()
    rType = models.CharField(max_length=100)
