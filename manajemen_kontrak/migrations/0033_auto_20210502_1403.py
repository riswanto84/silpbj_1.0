# Generated by Django 3.1.1 on 2021-05-02 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0032_lampirankontrak'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lampirankontrak',
            unique_together={('barang',)},
        ),
        migrations.RemoveField(
            model_name='lampirankontrak',
            name='penyedia',
        ),
    ]
