# Generated by Django 3.1.1 on 2021-04-30 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.CharField(max_length=500)),
                ('merk', models.CharField(blank=True, max_length=200, null=True)),
                ('tipe', models.CharField(blank=True, max_length=200, null=True)),
                ('satuan', models.CharField(max_length=100)),
                ('spesifikasi', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FotoBarang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, default='no-image.png', null=True, upload_to='')),
                ('nama_barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manajemen_kontrak.barang')),
            ],
        ),
    ]
