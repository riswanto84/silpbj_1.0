# Generated by Django 3.1.1 on 2021-07-13 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_ukpbj', '0058_auto_20210713_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paketpekerjaan',
            name='dokumen_surat_usulan',
            field=models.FileField(blank=True, null=True, upload_to='dokumen_surat_usulan'),
        ),
    ]