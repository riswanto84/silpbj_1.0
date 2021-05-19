# Generated by Django 3.1.1 on 2021-05-08 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manajemen_kontrak', '0081_auto_20210508_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontrak',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tandaterimadistribusi',
            name='nomor_tanda_terima',
            field=models.CharField(default='6315/cla27sP9', max_length=100),
        ),
    ]
