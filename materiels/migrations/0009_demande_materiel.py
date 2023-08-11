# Generated by Django 4.2.3 on 2023-08-09 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0001_initial'),
        ('materiels', '0008_alter_demandemateriel_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demande_Materiel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_demande', models.DateField()),
                ('date_reponse', models.DateField()),
                ('description', models.TextField()),
                ('status', models.CharField(default='pas encore traite', max_length=100)),
                ('demandeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employe.employe')),
                ('materiel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiels.materiel')),
            ],
        ),
    ]