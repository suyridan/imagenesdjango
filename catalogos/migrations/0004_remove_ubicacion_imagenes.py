# Generated by Django 4.2 on 2023-04-24 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalogos", "0003_ubicacion_imagenes"),
    ]

    operations = [
        migrations.RemoveField(model_name="ubicacion", name="imagenes",),
    ]