# Generated by Django 3.1.1 on 2021-06-02 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0019_auto_20210602_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pemeriksaanbarang',
            name='judul_pemeriksaan',
        ),
    ]