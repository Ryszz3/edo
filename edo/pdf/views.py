from django.shortcuts import render

from pdf.forms import UploadPdfForm
from pdf.models import PdfUploads


def upload_pdf(request):
    form = UploadPdfForm
    if request.method == "POST":
        form = UploadPdfForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.cleaned_data
            PdfUploads.objects.create(**form_data)
    return render(request, "upload_pdf.html", context={"title": "Загрузка PDF", "form": form})
