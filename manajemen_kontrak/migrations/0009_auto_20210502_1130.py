# Generated by Django 3.1.1 on 2021-05-02 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0008_kontrak_tanggal_kontrak'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kontrak',
            old_name='kode_mak',
            new_name='kode_kegiatan_output_akun',
        ),
        migrations.AlterField(
            model_name='kontrak',
            name='bentuk_kontrak',
            field=models.CharField(choices=[('Surat Perjanjian (kontrak)', 'Surat Perjanjian (kontrak)'), ('Surat Perintah Kerja', 'Surat Perintah Kerja'), ('Kuitansi', 'Kuitansi'), ('Surat Pesanan', 'Surat Pesanan'), ('Bukti Pembelian', 'Bukti Pembelian')], default='Surat Perintah Kerja', max_length=100),
        ),
        migrations.AlterField(
            model_name='kontrak',
            name='jenis_pekerjaan',
            field=models.CharField(choices=[('pengadaan barang', 'pengadaan barang'), ('pekerjaan konstruksi', 'pekerjaan konstruksi'), ('jasa konsultan', 'jasa konsultan'), ('jasa lainnya', 'jasa lainnya')], default='pengadaan barang', max_length=100),
        ),
    ]
