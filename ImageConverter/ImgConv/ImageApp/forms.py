from django import forms
import django
from django.forms import fields
from django.forms.models import fields_for_model

from . import models


class form(forms.ModelForm):
    
    class Meta():
        model=models.modelform
        fields=("Image",)
class option(forms.Form):
    Url=forms.CharField(label="Insert URL Here",required=False)
    choicesf=(('I2S','Image to Sketch Converter'),('I2C','Image to Cartoon Converter'),('I2BW','Image to Black and White Converter'),('I2B','Image to Blur Background Convert'))
    choicefield=forms.ChoiceField(choices=choicesf)
    def clean_Url(self):
        mainurl=self.cleaned_data['Url']
        import requests
        try:
            response = requests.get(mainurl)
         
        except requests.ConnectionError as exception:
            raise forms.ValidationError("URL is invalid")
        return mainurl