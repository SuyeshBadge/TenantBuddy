from django.db import models
from django.db.models.deletion import CASCADE
import os
# Create your models here.


def path_and_rename(instance, filename):
    upload_to = 'rooms/'
    ext = filename.split('.')[-1]
    filename = 'user{}room{}.{}'.format(
        instance.rOid.oId, instance.rOid.oRooms+1, ext)

    return os.path.join(upload_to, filename)


def pathrename(instance, filename):
    upload_to = 'profiles/'
    ext = filename.split('.')[-1]
    filename = '{}{}.{}'.format(instance.oId, instance.oFname, ext)

    return os.path.join(upload_to, filename)


class Owner(models.Model):
    oId = models.AutoField(primary_key=True)
    oFname = models.CharField(max_length=100)
    oLname = models.CharField(max_length=100)
    oEmail = models.EmailField(unique=True)
    oPassword = models.CharField(max_length=128)
    oMobile = models.BigIntegerField()
    oGender = models.CharField(max_length=4, null=True)
    oRooms = models.IntegerField(default=0)
    oDOB = models.DateField()
    oProfile = models.ImageField(upload_to=pathrename, default='avatarm.png')

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
    rPic = models.ImageField(upload_to=path_and_rename, null=True)
