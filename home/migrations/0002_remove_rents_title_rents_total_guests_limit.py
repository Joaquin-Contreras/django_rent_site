# Generated by Django 4.2.7 on 2023-11-21 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rents",
            name="title",
        ),
        migrations.AddField(
            model_name="rents",
            name="total_guests_limit",
            field=models.DecimalField(decimal_places=4, default=1, max_digits=15),
            preserve_default=False,
        ),
    ]
