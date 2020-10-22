from .models import squirrel
from django.forms import ModelForm

class Form(ModelForm):
    class Meta:
        model=squirrel
        fields=['latitude','longitude','squirrel_id','shift','date','age','primary_fur_color','location','specific_location','running','chasing','climbing','eating','foraging','other_Activities','kuks','quaas','moans','tail_flags','tail_twitches','approaches','indifferent','runs_From']
