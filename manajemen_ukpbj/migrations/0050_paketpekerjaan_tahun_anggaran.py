# Generated by Django 3.1.1 on 2021-07-12 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_ukpbj', '0049_paketpekerjaan_nilai_hasil_tender'),
    ]

    operations = [
        migrations.AddField(
            model_name='paketpekerjaan',
            name='tahun_anggaran',
            field=models.CharField(choices=[('2020', '2020'), ('2021', '2021')], default=2021, max_length=4),
        ),
    ]