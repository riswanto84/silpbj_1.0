# Generated by Django 3.1.1 on 2021-05-20 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manajemen_kontrak', '0002_tandaterimadistribusi_tanggal'),
    ]

    operations = [
        migrations.AddField(
            model_name='tandaterimadistribusi',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]