import json

from django.contrib.admin import action
from django.http import JsonResponse, HttpResponse, Http404, FileResponse
from django.shortcuts import render
from pathlib import Path
import os
from edo.settings import BASE_DIR
from word.models import Uploads
import pdfplumber


def show_uploads(request):

    context = {}
    data = Uploads.objects.all()
    context["data"] = data

    if request.method == "POST":
        if "publish" in request.POST:
            name = request.POST.get("publish")
            Uploads.objects.filter(file=f'uploads/word/{name}').update(status=True)

        if "unpublish" in request.POST:
            name = request.POST.get("unpublish")
            Uploads.objects.filter(file=f'uploads/word/{name}').update(status=False)

    return render(request, 'show_uploads.html', context)

def show_pdf(request):
    with pdfplumber.open("path/to/file.pdf") as pdf:
        first_page = pdf.pages[0]
        print(first_page.chars[0])

def download(request):
    print(request.POST)
    file_type = request.POST.get("file_name").split(".")[-1]
    print(file_type)
    if file_type == "docx":
        path = Path(BASE_DIR) / "uploads" / "word" / request.POST.get("file_name")
        print(path)

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