# Generated by Django 3.1.1 on 2021-07-12 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_ukpbj', '0019_auto_20210712_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegawaibersertifikat',
            name='sebagai_pokja_pemilihan',
            field=models.CharField(choices=[('Tidak', 'tidak'), ('Ya', 'ya')], default='Tidak', max_length=100),
        ),
    ]