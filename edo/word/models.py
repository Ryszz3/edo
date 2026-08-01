from django.db import models

class Uploads(models.Model):
    name = models.CharField(max_length=100, blank=False)
    file = models.FileField(upload_to="uploads/word")
    status = models.BooleanField(default=False)