import json

from django.contrib.admin import action
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from pathlib import Path
import os
from edo.settings import BASE_DIR
from word.models import Uploads


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


def process_file_ajax(request):
    req_data = decode(request.body)
    print(req_data)
    data = Uploads.objects.get(pk=req_data['file_index'])
    print(f"DATA: {data}")
    return HttpResponse


def decode(data):
    s_data = data.decode('utf-8')
    return json.loads(s_data)