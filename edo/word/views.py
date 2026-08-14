from django.shortcuts import render

from edo.settings import BASE_DIR
from word.forms import UploadWordForm
from word.models import Uploads

# def handle_uploaded_file(f):
#     with open(f"uploads/word/{f.name}", "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)



def upload_word(request):
    form = UploadWordForm()
    if request.method == 'POST':
        form = UploadWordForm(request.POST, request.FILES)


            # if form_data["name"]:
            #     print(f'CLEAN DATA: {form.cleaned_data}')
            #     Uploads.objects.create(**form_data)
        if form.is_valid():

            form_data = form.cleaned_data
            print(form_data.get("name"))
            # print(f'DATA: {form_data["name"]}')
            u = Uploads(**form_data)
            u.save()
            a = Uploads.objects.get(pk=u.pk)
            a.name = str(a.file).split(".")[-1]
            a.save()
            print(f"A: {a}")
    #         вывести все пдфки, кол во символов, страниц, слов


    return render(request, 'upload_word.html', {'form': form, 'title': 'Загрузить word файл'})


def process_file():
    return None