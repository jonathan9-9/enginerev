# Generated by Django 4.0.3 on 2023-07-26 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0004_automobilevo_import_href'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automobilevo',
            name='vin',
            field=models.CharField(max_length=1, null=True, unique=True),
        ),
    ]