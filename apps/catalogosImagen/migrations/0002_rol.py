# Generated by Django 4.2 on 2023-04-27 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalogosImagen", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Rol",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=200)),
                ("estatus", models.BooleanField()),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
