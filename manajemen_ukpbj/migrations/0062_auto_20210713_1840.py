# Generated by Django 3.1.1 on 2021-07-13 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_ukpbj', '0061_auto_20210713_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paketpekerjaan',
            name='file_surat_tugas',
            field=models.FileField(blank=True, null=True, upload_to='surat_tugas_pokja'),
        ),
    ]
