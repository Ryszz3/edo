from django.shortcuts import render
import os
import pandas as pd
from edo.settings import BASE_DIR
from excel.models import ExcelUploads


def handle_uploaded_file(f):
    with open(f"uploads/excel/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)



def upload_excel(request):
    if request.method == 'POST':
        file = request.FILES.get("file")
        ExcelUploads.objects.create(file=file)
    return render(request, 'upload_excel.html', {'title': 'Загрузить excel файл'})


def extract_sheets():
    path = BASE_DIR / "uploads" / "excel"
    for file in os.listdir(BASE_DIR / "uploads" / "excel"):
        if file.endswith(".xlsx"):
            xlfile = pd.ExcelFile(path / file)
            sheets = xlfile.sheet_names
            sheets_path = path / f'{file.split(".")[0]}_sheets'
            os.makedirs(sheets_path, exist_ok=True)

            for sheet in sheets:
                name = f'{file.split(".")[0]}_{sheet}'
                output_file = sheets_path / f'{name}.xlsx'
                print(path / name)
                print(name)
                data = xlfile.parse(sheet)
                data.to_excel(output_file, sheet_name=name, index=False, header=False)







