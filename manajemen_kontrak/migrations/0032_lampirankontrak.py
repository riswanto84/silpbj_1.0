# Generated by Django 3.1.1 on 2021-05-02 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0031_delete_lampirankontrak'),
    ]

    operations = [
        migrations.CreateModel(
            name='LampiranKontrak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kuantitas', models.IntegerField()),
                ('harga_satuan', models.DecimalField(decimal_places=2, max_digits=15)),
                ('barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manajemen_kontrak.barang')),
                ('nomor_kontrak', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manajemen_kontrak.kontrak')),
                ('penyedia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manajemen_kontrak.penyedia')),
            ],
            options={
                'unique_together': {('barang', 'penyedia')},
            },
        ),
    ]
