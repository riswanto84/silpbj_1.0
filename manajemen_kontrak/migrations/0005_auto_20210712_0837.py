# Generated by Django 3.1.1 on 2021-07-12 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0004_auto_20210624_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontrak',
            name='nomor_kontrak',
            field=models.CharField(default='.../1.5/PL.02.01/7/2021', max_length=200),
        ),
    ]