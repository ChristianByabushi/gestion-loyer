# Generated by Django 5.1.1 on 2024-10-02 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrat', '0007_alter_contrat_datedebut_alter_contrat_datefin'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrat',
            name='termes_du_contrat',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contrat',
            name='datedebut',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 2, 14, 11, 58, 516150)),
        ),
        migrations.AlterField(
            model_name='contrat',
            name='datefin',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 2, 14, 11, 58, 516150)),
        ),
    ]
