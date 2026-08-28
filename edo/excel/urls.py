from django.urls import path

from . import views

app_name = "excel"

urlpatterns = [
    path('excel/upload/', views.upload_excel, name='upload_excel'),
    path('excel/consolidate', views.consolidate_excel, name='consolidate_excel'),

]