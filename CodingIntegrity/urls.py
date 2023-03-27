
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('qr/', include('qr.urls'), name='qr'),
    path('admin/', admin.site.urls),
]
