# Generated by Django 3.1.1 on 2021-06-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tandaterimadistribusi',
            name='catatan',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
