# Generated by Django 3.1.1 on 2021-07-12 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_ukpbj', '0029_pegawaibersertifikat_skpokjapemilihan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skpokjapemilihan',
            name='nomor_sk',
            field=models.CharField(max_length=200),
        ),
    ]
