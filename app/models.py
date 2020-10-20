from django.db import models

class squirrel(models.Model):
    latitude=models.FloatField(blank=False)
    longitude=models.FloatField(blank=False)
    id=models.CharField(max_length=30,blank=False,unique=True)
    shift=models.CharField(max_length=30,blank=False)
    date=models.CharField(max_length=30,blank=False)
    age=models.CharField(max_length=30,blank=False)
    primary_fur_color=models.CharField(max_length=30,blank=True)
    location=models.CharField(max_length=30,blank=True)
    specific_location=models.CharField(max_length=30,blank=True)
    Running=models.BooleanField(blank=True)
    Chasing=models.BooleanField(blank=True)
    Climbing=models.BooleanField(blank=True)
    Eating=models.BooleanField(blank=True)
    Foraging=models.BooleanField(blank=True)
    Other_Activities=models.CharField(max_length=30, blank=True)
    Kuks=models.BooleanField(blank=True)
    Quaas=models.BooleanField(blank=True)
    Moans=models.BooleanField(blank=True)
    Tail_Flags=models.BooleanField(blank=True)
    Tail_Twitches=models.BooleanField(blank=True)
    Approaches=models.BooleanField(blank=True)
    Indifferent=models.BooleanField(blank=True)
    Runs_From=models.BooleanField(blank=True)

class apprequest(models.Model):
    squi=models.ForeignKey('app.squirrel',on_delete=models.CASCADE)




