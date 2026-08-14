from django.urls import path

from . import views

app_name = "pdf"

urlpatterns = [path('pdf/upload/', views.upload_pdf, name='upload_pdf'),

]