from django import forms
from django.forms import ModelForm
from . models import Event

class UploadFileForm(forms.Form):
    file = forms.FileField()

class RegisterEvent(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        
class GenerateQRForm(forms.Form):
    generate = forms.BooleanField(initial=True)
