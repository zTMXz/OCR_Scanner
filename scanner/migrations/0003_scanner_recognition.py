# Generated by Django 4.2.2 on 2023-06-13 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scanner", "0002_scanner_user_alter_scanner_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="scanner",
            name="recognition",
            field=models.TextField(blank=True),
        ),
    ]