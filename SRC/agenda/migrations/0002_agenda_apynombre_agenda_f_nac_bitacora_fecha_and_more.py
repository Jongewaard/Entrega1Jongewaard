# Generated by Django 4.0.6 on 2022-08-06 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='apynombre',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AddField(
            model_name='agenda',
            name='f_nac',
            field=models.DateField(default=datetime.datetime(2022, 8, 6, 12, 59, 35, 434237)),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2022, 8, 6, 12, 59, 35, 434237)),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='sucesos',
            field=models.CharField(default='default', max_length=300),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='titulo',
            field=models.CharField(default='titulo', max_length=20),
        ),
        migrations.AddField(
            model_name='calendario',
            name='f_aviso_evento',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 6, 12, 59, 35, 434237)),
        ),
        migrations.AddField(
            model_name='calendario',
            name='f_evento',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 6, 12, 59, 35, 434237)),
        ),
        migrations.AddField(
            model_name='calendario',
            name='nombre_evento',
            field=models.CharField(default='evento', max_length=100),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='e_mail',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='momento',
            field=models.TimeField(default=datetime.datetime(2022, 8, 6, 12, 59, 35, 434237)),
        ),
    ]