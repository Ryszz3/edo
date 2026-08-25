from django.db import models

from edo.settings import BASE_DIR


class ExcelUploads(models.Model):
    file = models.FileField(upload_to=BASE_DIR / 'uploads' / 'excel')
    created_at = models.DateTimeField(auto_now=True)

class ExcelSheets(models.Model):
    name = models.CharField(max_length=100)
    source = models.ForeignKey(ExcelUploads, on_delete=models.CASCADE)

class ConsolidatedExcel(models.Model):
    name = models.CharField(max_length=255, blank=False)
    files = models.ForeignKey(ExcelUploads, on_delete=models.PROTECT)
    file = models.FileField(upload_to=BASE_DIR / 'uploads' / 'excel')
    created_at = models.DateTimeField(auto_now=True)