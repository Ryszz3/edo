
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(' ', include('ai.urls')),
    path(' ', include('exel.urls')),
    path(' ', include('pdf.urls')),
    path(' ', include('user.urls')),
    path(' ', include('word.urls')),

]
