from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path('user/show_uploads/', views.show_uploads, name="show_uploads"),
    path('process-file-ajax/', views.process_file_ajax, name='process_file_ajax')
]