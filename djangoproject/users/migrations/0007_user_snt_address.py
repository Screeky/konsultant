# Generated by Django 4.1.7 on 2023-04-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_alter_user_snt_snt_id_delete_snt"),
    ]

    operations = [
        migrations.AddField(
            model_name="user_snt",
            name="address",
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
