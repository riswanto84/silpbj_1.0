# Generated by Django 3.1.1 on 2021-05-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tandaterimadistribusi',
            name='tanggal',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
