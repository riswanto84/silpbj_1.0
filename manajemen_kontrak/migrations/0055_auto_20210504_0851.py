# Generated by Django 3.1.1 on 2021-05-04 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0054_auto_20210504_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tandaterimadistribusi',
            name='nomor_tanda_terima',
            field=models.CharField(default='1721/AYthMZEb', max_length=100),
        ),
    ]
