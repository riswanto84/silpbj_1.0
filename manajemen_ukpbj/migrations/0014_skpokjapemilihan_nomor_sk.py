# Generated by Django 3.1.1 on 2021-07-12 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_ukpbj', '0013_auto_20210712_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='skpokjapemilihan',
            name='nomor_sk',
            field=models.CharField(default='Nomor 23/HUK/2020', max_length=200),
        ),
    ]
