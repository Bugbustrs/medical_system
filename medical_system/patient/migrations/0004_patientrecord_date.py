# Generated by Django 2.2.6 on 2019-10-12 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_patientrecord_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientrecord',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]