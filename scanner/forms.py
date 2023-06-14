from django import forms
from .models import Scanner


class ScannerForm(forms.ModelForm):
    description = forms.CharField(max_length=255, required=False)
    class Meta:
        model = Scanner
        fields = ('description', 'image')