# Generated by Django 4.2.3 on 2023-07-24 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0001_initial'),
        ('materiels', '0004_materiel_en_panne'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemandeMateriel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut_utilisation', models.DateField()),
                ('description', models.TextField()),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employe.employe')),
                ('materiel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiels.materiel')),
            ],
        ),
    ]