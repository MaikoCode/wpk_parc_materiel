# Generated by Django 4.2.3 on 2023-07-18 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materiels', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materiel',
            name='is_taken',
        ),
    ]
