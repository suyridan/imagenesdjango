# Generated by Django 4.2 on 2023-04-24 03:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("acervos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AcervoCliente",
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
                ("name", models.TextField(max_length=255)),
                ("estatus", models.BooleanField()),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
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
            name="LicenciaTipo",
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
                ("name", models.TextField(max_length=255)),
                ("estatus", models.BooleanField(default=True)),
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
        migrations.AlterModelOptions(
            name="acervo",
            options={
                "ordering": ["tn_order"],
                "verbose_name": "Acervo",
                "verbose_name_plural": "Acervos",
            },
        ),
        migrations.AddField(
            model_name="acervo",
            name="tn_ancestors_count",
            field=models.PositiveIntegerField(
                default=0, editable=False, verbose_name="Ancestors count"
            ),
        ),
        migrations.AddField(
            model_name="acervo",
            name="tn_ancestors_pks",
            field=models.TextField(
                blank=True, default="", editable=False, verbose_name="Ancestors pks"
            ),
        ),
        migrations.AddField(
            model_name="acervo",
            name="tn_children_count",
            field=models.PositiveIntegerField(
                default=0, editable=False, verbose_name="Children count"
            ),
        ),
        migrations.AddField(
            model_name="acervo",
            name="tn_children_pks",
            field=models.TextField(
                blank=True, default="", editable=False, verbose_name="Children pks"
            ),
        ),
        migrations.AddField(
            model_name="acervo",
            name="tn_depth",
            field=models.PositiveIntegerField(
                default=0,
                editable=False,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10),
                ],
                verbose_name="Depth",
            ),
        ),
        migrations.AddField(
            model_name="acervo",
            name="tn_descendants_count",
            field=models.PositiveIntegerField(
                default=0, editable=False, verbose_name="Descendants count"
            ),
        ),
        migrations.AddField(
            model_name="acervo",
            name="tn_descendants_pks",
            field=models.TextField(
                blank=True, default="", editable=False, verbose_name="Descendants pks"
            ),
        ),
        migrations.AddField(
            model_name="acervo",
            name="tn_index",
            field=models.PositiveIntegerField(
                default=0, editable=False, verbose_name="Index"
            ),
        ),
        migrations.AddField(
            model_name="acervo",
            name="tn_level",
            field=models.PositiveIntegerField(
                default=1,
                editable=False,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(10),
                ],
                verbose_name="Level",
            ),
        ),
        migrations.AddField(
            model_name="acervo",
            name="tn_order",
            field=models.PositiveIntegerField(
                default=0, editable=False, verbose_name="Order"
            ),
        ),
        migrations.AddField(
            model_name="acervo",
            name="tn_parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tn_children",
                to="acervos.acervo",
                verbose_name="Parent",
            ),
        ),
        migrations.AddField(
            model_name="acervo",
            name="tn_priority",
            field=models.PositiveIntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(9999),
                ],
                verbose_name="Priority",
            ),
        ),
        migrations.AddField(
            model_name="acervo",
            name="tn_siblings_count",
            field=models.PositiveIntegerField(
                default=0, editable=False, verbose_name="Siblings count"
            ),
        ),
        migrations.AddField(
            model_name="acervo",
            name="tn_siblings_pks",
            field=models.TextField(
                blank=True, default="", editable=False, verbose_name="Siblings pks"
            ),
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
                ("titulo", models.CharField(max_length=255)),
                ("estatus", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(auto_now=True)),
                (
                    "acervo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="acervos.acervo"
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="Licencia",
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
                ("vigencia", models.DateTimeField(auto_now_add=True)),
                (
                    "AcervoCliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="acervos.acervocliente",
                    ),
                ),
                ("VisualImagenes", models.ManyToManyField(to="acervos.visualimagen")),
                (
                    "tipo_licencia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="acervos.licenciatipo",
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
                ("titulo", models.CharField(max_length=255)),
                ("estatus", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(auto_now=True)),
                (
                    "contenedor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="acervos.acervo"
                    ),
                ),
            ],
            options={"abstract": False,},
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
