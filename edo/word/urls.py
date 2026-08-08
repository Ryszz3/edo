from django.urls import path
from . import views

app_name = "word"

urlpatterns = [
    path('word/upload/', views.upload_word, name='upload_word'),

]