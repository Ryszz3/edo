from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path('user/show_uploads', views.show_uploads, name="show_uploads")
]