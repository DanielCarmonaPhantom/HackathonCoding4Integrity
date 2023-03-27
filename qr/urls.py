from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('<int:medicine_id>', views.medicine_detail, name='medicine_detail'),
    path('medicine/<str:serial>', views.medicine_serial, name="'medicine_serial")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)