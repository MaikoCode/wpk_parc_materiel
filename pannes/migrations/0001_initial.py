# Generated by Django 4.2.3 on 2023-07-18 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materiels', '0003_materiel_is_taken'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_panne', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('resolue', models.BooleanField(default=False)),
                ('materiel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiels.materiel')),
            ],
        ),
    ]
