# Generated by Django 4.2 on 2023-04-24 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("acervos", "0006_alter_acervo_name_alter_licenciatipo_name"),
    ]

    operations = [
        migrations.RemoveField(model_name="fisicaimagen", name="ubicacion",),
    ]
