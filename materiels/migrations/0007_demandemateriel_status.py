# Generated by Django 4.2.3 on 2023-07-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiels', '0006_rename_date_debut_utilisation_demandemateriel_date_debut_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='demandemateriel',
            name='status',
            field=models.CharField(default='pas encore traite'),
        ),
    ]