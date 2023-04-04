# Generated by Django 4.1.7 on 2023-04-01 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SNT",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="User_snt",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("last_name", models.CharField(blank=True, max_length=30)),
                ("first_name", models.CharField(blank=True, max_length=30)),
                ("middle_name", models.CharField(blank=True, max_length=30)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_gover", models.BooleanField(default=False)),
                ("is_verif", models.BooleanField(default=False)),
                (
                    "snt",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.snt"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]