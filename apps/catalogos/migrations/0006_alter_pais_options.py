# Generated by Django 4.2 on 2023-04-27 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalogos", "0005_estado_pais_municipio_estado_pais"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="pais",
            options={"verbose_name": "Pais", "verbose_name_plural": "Paises"},
        ),
    ]
