from .models import apprequest
from django.forms import ModelForm

class apprequestform(ModelForm):
    class Meta:
        model=apprequest
        fields=['squi']