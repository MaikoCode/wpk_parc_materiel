# Generated by Django 4.2.3 on 2023-07-24 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mouvementmateriels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mouvementmateriel',
            name='actionType',
            field=models.CharField(default='acquisition', max_length=30),
        ),
    ]
