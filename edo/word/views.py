from django.shortcuts import render
from word.models import Uploads

# def handle_uploaded_file(f):
#     with open(f"uploads/word/{f.name}", "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)



def upload_word(request):
    if request.method == 'POST':
        u = Uploads(file=request.FILES.get("file_upload"))
        u.save()

    return render(request, 'upload_word.html', {'title': 'Загрузить word файл'})


