from django import forms

from word.models import Uploads


class UploadWordForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = ["file", "status"]