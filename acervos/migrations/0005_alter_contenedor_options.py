# Generated by Django 4.2 on 2023-04-24 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("acervos", "0004_fisicaimagen_ubicacion_visualimagen_ubicacion"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contenedor",
            options={
                "ordering": ["tn_order"],
                "verbose_name": "Contenedor",
                "verbose_name_plural": "Contenedores",
            },
        ),
    ]
