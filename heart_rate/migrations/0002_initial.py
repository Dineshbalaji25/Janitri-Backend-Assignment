# Generated by Django 4.2.19 on 2025-02-18 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
        ('heart_rate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='heartrate',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient'),
        ),
    ]
