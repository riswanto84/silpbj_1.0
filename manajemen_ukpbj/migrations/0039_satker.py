# Generated by Django 3.1.1 on 2021-07-12 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_ukpbj', '0038_paketpekerjaan_tanggal_usulan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Satker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_satker', models.CharField(max_length=300)),
            ],
        ),
    ]