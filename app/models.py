from django.db import models

class squirrel(models.Model):
    latitude=models.FloatField(label='latitude')
    longitude=models.FloatField(label='longitude')
    id=models.CharField(max_length=30,label='id')
    shift=models.CharField(max_length=30,label='shift')
    date=models.CharField(max_length=30,label='date')
    age=models.CharField(max_length=30,label='age')
class apprequest(models.Model):
    squi=models.ForeignKey('app.squirrel',on_delete=models.CASCADE)




