# Generated by Django 3.1.1 on 2021-06-02 14:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0006_auto_20210602_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pemeriksaanbarang',
            name='item_pekerjaan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manajemen_kontrak.lampirankontrak'),
        ),
        migrations.AlterField(
            model_name='pemeriksaanbarang',
            name='tanggal_pemeriksaan',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
