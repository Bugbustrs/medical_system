# Generated by Django 2.2.6 on 2019-10-12 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20191012_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientrecord',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.Patient'),
        ),
    ]