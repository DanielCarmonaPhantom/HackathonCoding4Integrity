import os.path
import qrcode
import hashlib
from datetime import date
from datetime import datetime

from django.shortcuts import render


from io import BytesIO

# Create your views here.
from django.shortcuts import render
from django.conf import settings

from django.core.files.storage import default_storage

from .models import QR_medicine, Medicine_catalog, Laboratory

def index(request):

    texto = "Medicinas"
    batchs = QR_medicine.objects.all()
    medicines_catalog = Medicine_catalog.objects.all()

    if request.method == 'POST':
        laboratory_form = request.POST.get('laboratory')
        medicine_form = request.POST.get('medicine')
        batch_form = request.POST.get('batch')
        expiretAt = request.POST.get('expiretAT')

        texto = laboratory_form + "." + medicine_form + "." + batch_form + "." + str(datetime.now().date()).replace("-", ".") + "." +expiretAt.replace("-", ".")

        texto = texto.encode("utf-8")

        QR_medicine.objects.create(
            laboratory_id= Laboratory.objects.get(id=laboratory_form),
            medicine_id= Medicine_catalog.objects.get(id=medicine_form),
            serial = hashlib.sha256(texto).hexdigest(),
            batch= batch_form,
            expiration_at = expiretAt
        )




    context = {
        'texto': texto,
        'medicines_catalog': medicines_catalog,
        'batchs' : batchs
    }
    return render(request, 'QR/index.html', context)

def medicine_detail(request, medicine_id):

    qr_medicine = QR_medicine.objects.get(id = medicine_id)

    qr = qrcode.QRCode(version=1, box_size=10, border=5)

    identificador = qr_medicine.serial


    qr.add_data(identificador)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    path_img = os.path.join('qr', settings.MEDIA_ROOT,  'images', f'{identificador}.png')
    img.save(path_img)  # guarde el archivo en su sistema de archivos

    path_img_relative= os.path.join('media' ,'images', f'{identificador}.png')





    context = {
        'batch': qr_medicine,
        'medicine': Medicine_catalog.objects.get(id=qr_medicine.medicine_id.id),
        'path_img_relative': path_img_relative
    }

    return render(request, 'QR/medicine_detail.html', context)


def medicine_serial(request, medicine_serial):


    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    identificador = medicine_serial
    img = qr.make_image(fill_color="black", back_color="white")

    path_img = os.path.join('qr', settings.MEDIA_ROOT, 'images', f'{identificador}.png')
    img.save(path_img)  # guarde el archivo en su sistema de archivos


    context = {

    }

    return render(request, 'QR/medicine_serial.html', context)