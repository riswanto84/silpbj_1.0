# Generated by Django 3.1.1 on 2021-05-04 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0058_auto_20210504_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='barang',
            name='modified_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='tandaterimadistribusi',
            name='nomor_tanda_terima',
            field=models.CharField(default='1379/zFS8U9tt', max_length=100),
        ),
    ]
