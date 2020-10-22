from django.db import models

class squirrel(models.Model):
    latitude=models.FloatField(blank=False)
    longitude=models.FloatField(blank=False)
    squirrel_id=models.CharField(max_length=30,primary_key=True)
    shift=models.CharField(max_length=30,blank=False)
    date=models.CharField(max_length=30,blank=False)
    age=models.CharField(max_length=30,blank=False)
    primary_fur_color=models.CharField(max_length=30,blank=True)
    location=models.CharField(max_length=30,blank=True)
    specific_location=models.CharField(max_length=30,blank=True)
    running=models.BooleanField(blank=True)
    chasing=models.BooleanField(blank=True)
    climbing=models.BooleanField(blank=True)
    eating=models.BooleanField(blank=True)
    foraging=models.BooleanField(blank=True)
    other_Activities=models.CharField(max_length=30, blank=True)
    kuks=models.BooleanField(blank=True)
    quaas=models.BooleanField(blank=True)
    moans=models.BooleanField(blank=True)
    tail_flags=models.BooleanField(blank=True)
    tail_twitches=models.BooleanField(blank=True)
    approaches=models.BooleanField(blank=True)
    indifferent=models.BooleanField(blank=True)
    runs_From=models.BooleanField(blank=True)

class apprequest(models.Model):
    squi=models.ForeignKey('app.squirrel',on_delete=models.CASCADE)




