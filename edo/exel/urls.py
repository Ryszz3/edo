from django.urls import path

from . import views

app_name = "exel"

urlpatterns = [
    path('exel/upload/', views.upload_exel, name='upload_exel')

]