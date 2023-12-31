# Generated by Django 4.0.3 on 2023-07-26 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0002_alter_appointment_finished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='finished',
        ),
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(default='Created', max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='technician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='service_rest.technician'),
        ),
        migrations.AlterField(
            model_name='automobilevo',
            name='vin',
            field=models.CharField(default=False, max_length=1, unique=True),
        ),
    ]
