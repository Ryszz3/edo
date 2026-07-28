from django.urls import path
from . import views

app_name = "word"

urlpatterns = [
    path('', views.upload_word, name='upload_word'),
]