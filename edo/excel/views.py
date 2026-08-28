from pathlib import Path

from django.shortcuts import render
import os
import pandas as pd
from edo.settings import BASE_DIR
from excel.models import ExcelUploads, ExcelSheets


def handle_uploaded_file(f):
    with open(f"uploads/excel/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_excel(request):
    if request.method == 'POST':
        file = request.FILES.get("file")
        e = ExcelUploads(file=file)
        e.save()
        short_file_name = str(e.file).split("/")[-1].split(".")[0]
        print(f"short_file_name: {short_file_name}")
        xlfile = pd.ExcelFile(e.file.path)
        sheets = xlfile.sheet_names
        sheets_path = Path(f"uploads/excel/{short_file_name}_sheets")
        os.mkdir(sheets_path)
        for sheet in sheets:
            sheet_name = f"{short_file_name}_{sheet}"
            output_file = sheets_path / f'{sheet_name}.xlsx'
            data = xlfile.parse(sheet)
            data.to_excel(output_file, sheet_name=sheet_name, index=False, header=False)
            s = ExcelSheets(name=f'{sheet_name}.xlsx', file=str(sheets_path / f"{sheet_name}.xlsx"), source=e)
            s.save()
    return render(request, 'upload_excel.html', {'title': 'Загрузить excel файл'})

def consolidate_excel(request):
    if request.method == "POST":
        data = request.POST.get("consolidate")
        for pk in data:
            sheets_to_consolidate = ExcelSheets.objects.filter(pk=pk)
            print(sheets_to_consolidate)







