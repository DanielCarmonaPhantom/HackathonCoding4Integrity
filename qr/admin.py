from django.contrib import admin

# Register your models here.

from .models import Laboratory, Medicine_catalog, QR_medicine

admin.site.register(Laboratory)
admin.site.register(Medicine_catalog)
admin.site.register(QR_medicine)
