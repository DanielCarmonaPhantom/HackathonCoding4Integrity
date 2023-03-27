# Generated by Django 4.1.7 on 2023-03-26 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('medicine_provider', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine_catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='QR_medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=255)),
                ('batch', models.IntegerField()),
                ('expiration_at', models.DateTimeField()),
                ('valitation', models.BooleanField(blank=True, default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('laboratory_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qr.laboratory')),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qr.medicine_catalog')),
            ],
        ),
    ]