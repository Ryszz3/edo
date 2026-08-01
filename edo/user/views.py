from django.shortcuts import render
from pathlib import Path
import os
from edo.settings import BASE_DIR


def show_uploads(request):
    p = Path('uploads')
    context = {}
    dir = os.listdir(BASE_DIR/"uploads/word")

    context["word"] = dir
    print(f"PRINT: {context}")

    return render(request, 'show_uploads.html', context)
