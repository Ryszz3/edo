from django import forms

from pdf.models import PdfUploads


class UploadPdfForm(forms.ModelForm):
    class Meta:
        model = PdfUploads
        fields = ["file"]