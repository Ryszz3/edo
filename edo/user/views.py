import json

from django.contrib.admin import action
from django.http import JsonResponse, HttpResponse, Http404, FileResponse
from django.shortcuts import render
from pathlib import Path
import os
from edo.settings import BASE_DIR
from excel.models import ExcelUploads
from word.models import Uploads
from pdf.models import PdfUploads
import pdfplumber


def show_uploads(request):
    context = {}


    word_data = Uploads.objects.all()
    context["data"] = {}
    context["data"]["word"] = word_data
    context["data"]["pdf"] = show_pdf()


    if request.method == "POST":
        if "publish" in request.POST:
            name = request.POST.get("publish")
            Uploads.objects.filter(file=f'uploads/word/{name}').update(status=True)

        if "unpublish" in request.POST:
            name = request.POST.get("unpublish")
            Uploads.objects.filter(file=f'uploads/word/{name}').update(status=False)

    return render(request, 'show_uploads.html', context)

def show_pdf():
    result = {}
    counter = 0
    pdf = PdfUploads.objects.all()
    for p in pdf:
        if os.path.isfile(BASE_DIR / str(p.file)):
            chars = ""
            words = 0
            counter += 1
            with pdfplumber.open(p.file) as f:
                for page in f.pages:
                    chars += page.extract_text()
                    words += len(page.extract_words())
                lines = chars.splitlines()
                result[f"pdf_file_{counter}"] = {"pk": p.pk, "name": str(p.file).split("/")[-1], "chars": len(chars), "words": words, "lines": len(lines)}
    return result

def show_excel():
    excel = ExcelUploads.objects.all()
    for e in excel:
        os.path.isfile(BASE_DIR / str(e.file))
        pass




def download_word(request):
    print(request.POST)
    file_type = request.POST.get("file_path").split(".")[-1]
    print(file_type)
    if file_type == "docx":
        print(f'BASE_DIR: {Path(BASE_DIR)}')
        path = Path(BASE_DIR) / request.POST.get("file_path")
        print(f" Path: {path}")

        if not path.is_file():
            raise Http404("Файл не найден")

        return FileResponse(
            path.open("rb"),
            as_attachment=True,
            filename=path,
        )


def process_file_ajax(request):
    req_data = decode(request.body)
    print(req_data)
    data = Uploads.objects.get(pk=req_data['file_index'])
    print(f"DATA: {data}")
    return HttpResponse


def decode(data):
    s_data = data.decode('utf-8')
    return json.loads(s_data)