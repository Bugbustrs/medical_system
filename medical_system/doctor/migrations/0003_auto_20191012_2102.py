# Generated by Django 2.2.6 on 2019-10-12 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_auto_20191012_2007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='second_name',
            new_name='surname',
        ),
    ]
