# Generated by Django 3.1.1 on 2021-07-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_ukpbj', '0004_pegawaibersertifikat_nomor_hp'),
    ]

    operations = [
        migrations.AddField(
            model_name='pegawaibersertifikat',
            name='nomor_sertifikat',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]