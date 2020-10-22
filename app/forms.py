from .models import squirrel
from django.forms import ModelForm

class Form(ModelForm):
    class Meta:
        model=squirrel
        fields=['__all__']
