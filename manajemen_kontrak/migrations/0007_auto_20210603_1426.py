# Generated by Django 3.1.1 on 2021-06-03 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0006_auto_20210525_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='satuan',
            field=models.CharField(choices=[('unit', 'unit'), ('buah', 'buah'), ('roll', 'roll'), ('meter', 'meter'), ('m2', 'm2'), ('m1', 'm1'), ('set', 'set'), ('ls', 'ls'), ('pcs', 'pcs'), ('rim', 'rim'), ('buku', 'buku'), ('hari', 'hari'), ('minggu', 'minggu'), ('bulan', 'bulan'), ('tahun', 'tahun')], max_length=100),
        ),
        migrations.AlterField(
            model_name='kontrak',
            name='nomor_kontrak',
            field=models.CharField(default='.../1.5/PL.02.01/6/2021', max_length=200),
        ),
    ]
