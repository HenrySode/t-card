from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class GenerateQRForm(forms.Form):
    generate = forms.BooleanField(initial=True)
