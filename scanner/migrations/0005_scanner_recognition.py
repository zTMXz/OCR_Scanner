# Generated by Django 4.2.2 on 2023-06-13 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scanner", "0004_remove_scanner_recognition_scanhistory"),
    ]

    operations = [
        migrations.AddField(
            model_name="scanner",
            name="recognition",
            field=models.TextField(blank=True),
        ),
    ]
