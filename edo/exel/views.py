from django.shortcuts import render

def handle_uploaded_file(f):
    with open(f"uploads/exel/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)



def upload_exel(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES["file_upload"])
    return render(request, 'upload_exel.html', {'title': 'Загрузить exel файл'})
