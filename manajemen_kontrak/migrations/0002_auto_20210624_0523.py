# Generated by Django 3.1.1 on 2021-06-24 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SatuanBarang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satuan', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='barang',
            name='satuan',
            field=models.CharField(choices=[('unit', 'unit'), ('buah', 'buah'), ('ls', 'ls'), ('hari', 'hari'), ('m', 'm'), ('m1', 'm1'), ('m2', 'm2'), ('m3', 'm3'), ('bh', 'bh'), ('meter', 'meter'), ('pcs', 'pcs'), ('buku', 'buku'), ('rim', 'rim'), ('set', 'set'), ('roll', 'roll'), ('minggu', 'minggu'), ('bulan', 'bulan'), ('tahun', 'tahun'), ('lembar', 'lembar'), ('box', 'box')], max_length=100),
        ),
    ]
