# Generated by Django 4.1.7 on 2023-04-05 11:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("docs", "0004_testdoc"),
    ]

    operations = [
        migrations.AddField(
            model_name="testdoc",
            name="file",
            field=models.FileField(default=0, upload_to="uploads/"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="testdoc",
            name="name",
            field=models.CharField(default="file", max_length=100),
            preserve_default=False,
        ),
    ]
