from django.db import models

# Create your models here.

class Laboratory(models.Model):
    name = models.CharField(max_length=255, blank=False)
    medicine_provider = models.CharField(max_length= 255, blank=False)

    def __str__(self):
        return self.name

class Medicine_catalog(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class QR_medicine(models.Model):
    laboratory_id = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(Medicine_catalog, on_delete=models.CASCADE)

    serial = models.CharField(max_length=255, blank=False)

    batch = models.IntegerField(blank=False)

    expiration_at = models.DateTimeField(blank=False)
    valitation = models.BooleanField(default=False, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.serial


