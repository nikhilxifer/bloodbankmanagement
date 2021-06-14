from django.db import models


# Create your models here.


class search1(models.Model):
    ID=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=120)
    State=models.CharField(max_length=120)
    City=models.CharField(max_length=120)
    Contact=models.IntegerField()

    