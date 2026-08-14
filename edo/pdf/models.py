from django.db import models

class PdfUploads(models.Model):
    file = models.FileField(upload_to="uploads/pdf")
    created_at = models.DateTimeField(auto_now_add=True)

