# Generated by Django 3.1.1 on 2021-07-12 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_ukpbj', '0054_auto_20210712_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='paketpekerjaan',
            name='keterangan',
            field=models.TextField(blank=True, null=True),
        ),
    ]
