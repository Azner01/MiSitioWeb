# Generated by Django 5.1 on 2024-09-05 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entrada",
            name="fecha_publicacion",
            field=models.DateTimeField(auto_created=True),
        ),
    ]
