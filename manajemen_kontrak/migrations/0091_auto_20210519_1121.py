# Generated by Django 3.1.1 on 2021-05-19 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0090_auto_20210519_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontrak',
            name='penyedia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manajemen_kontrak.penyedia'),
        ),
    ]
