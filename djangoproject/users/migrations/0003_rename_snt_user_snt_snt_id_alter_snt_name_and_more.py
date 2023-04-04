# Generated by Django 4.1.7 on 2023-04-02 17:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_snt_phone_alter_user_snt_password"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user_snt",
            old_name="snt",
            new_name="snt_id",
        ),
        migrations.AlterField(
            model_name="snt",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="user_snt",
            name="password",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="user_snt",
            name="phone",
            field=models.CharField(blank=True, max_length=15),
        ),
    ]