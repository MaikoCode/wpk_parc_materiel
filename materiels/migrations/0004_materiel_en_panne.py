# Generated by Django 4.2.3 on 2023-07-18 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiels', '0003_materiel_is_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='materiel',
            name='en_panne',
            field=models.BooleanField(default=False),
        ),
    ]
