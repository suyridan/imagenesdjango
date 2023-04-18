# Generated by Django 4.2 on 2023-04-18 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("acervos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Autor",
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
        migrations.CreateModel(
            name="Editor",
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
        migrations.CreateModel(
            name="Personaje",
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
        migrations.CreateModel(
            name="Reprografia",
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
        migrations.CreateModel(
            name="VisualImagen",
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
                (
                    "acervo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="acervos.acervo"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FisicaImagen",
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
                (
                    "visual",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="acervos.visualimagen",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ArchivistaHistoria",
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
                (
                    "fisica",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="acervos.fisicaimagen",
                    ),
                ),
            ],
        ),
    ]
