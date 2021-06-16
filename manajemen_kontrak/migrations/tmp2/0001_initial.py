# Generated by Django 3.1.1 on 2021-06-04 14:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.CharField(blank=True, max_length=500, null=True)),
                ('merk', models.CharField(blank=True, max_length=200, null=True)),
                ('tipe', models.CharField(blank=True, max_length=200, null=True)),
                ('satuan', models.CharField(choices=[('unit', 'unit'), ('buah', 'buah'), ('ls', 'ls'), ('hari', 'hari'), ('m1', 'm1'), ('m2', 'm2'), ('bh', 'bh'), ('meter', 'meter'), ('pcs', 'pcs'), ('buku', 'buku'), ('rim', 'rim'), ('set', 'set'), ('roll', 'roll'), ('minggu', 'minggu'), ('bulan', 'bulan'), ('tahun', 'tahun')], max_length=100)),
                ('spesifikasi_dan_gambar', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('modified_by', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kontrak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor_dipa', models.CharField(default='027.01.1.440121/2020', max_length=500)),
                ('tanggal_dipa', models.DateField(default='2019-11-21')),
                ('tahun_anggaran', models.CharField(choices=[('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029'), ('2030', '2030')], default=2021, max_length=4)),
                ('nomor_kontrak', models.CharField(default='.../1.5/PL.02.01/6/2021', max_length=200)),
                ('judul_kontrak', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('Final', 'Final'), ('Draft', 'Draft')], default='Final', max_length=100)),
                ('tanggal_kontrak', models.DateField(default=datetime.datetime.now)),
                ('tanggal_berakhir_kontrak', models.DateField(default=datetime.datetime.now)),
                ('kode_kegiatan_output_akun', models.CharField(default='2228.962.004/052/A/532111', max_length=50)),
                ('jenis_pekerjaan', models.CharField(choices=[('Pengadaan Barang', 'Pengadaan Barang'), ('Pekerjaan Konstruksi', 'Pekerjaan Konstruksi'), ('Jasa konsultan', 'Jasa konsultan'), ('Jasa lainnya', 'Jasa lainnya')], default='pengadaan barang', max_length=100)),
                ('bentuk_kontrak', models.CharField(choices=[('Surat Perjanjian (kontrak)', 'Surat Perjanjian (kontrak)'), ('Surat Perintah Kerja', 'Surat Perintah Kerja'), ('Kuitansi', 'Kuitansi'), ('Surat Pesanan', 'Surat Pesanan'), ('Bukti Pembelian', 'Bukti Pembelian')], default='Surat Perintah Kerja', max_length=100)),
                ('cara_pembayaran', models.CharField(choices=[('Bulanan', 'Bulanan'), ('Bertahap/Termin', 'Bertahap/Termin'), ('Sekaligus', 'Sekaligus')], default='Sekaligus', max_length=200)),
                ('ketentuan_sanksi', models.CharField(blank=True, default='Denda 1 ‰ untuk setiap hari keterlambatan dari biaya / harga keseluruhan (sebelum PPn)', max_length=500, null=True)),
                ('dokumen_pengadaan', models.FileField(blank=True, max_length=255, null=True, upload_to='dokumenpengadaan/')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('modified_by', models.IntegerField(blank=True, null=True)),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LampiranKontrak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kuantitas', models.DecimalField(decimal_places=2, max_digits=6)),
                ('harga_satuan', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('modified_by', models.IntegerField(blank=True, null=True)),
                ('barang', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manajemen_kontrak.barang')),
                ('nomor_kontrak', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manajemen_kontrak.kontrak')),
            ],
        ),
        migrations.CreateModel(
            name='Penyedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_perusahaan', models.CharField(max_length=300)),
                ('alamat_perusahaan', models.CharField(max_length=500)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('npwp_perusahaan', models.CharField(blank=True, max_length=20, null=True)),
                ('nomor_rekening', models.CharField(blank=True, max_length=100, null=True)),
                ('bank', models.CharField(blank=True, max_length=200, null=True)),
                ('direktur', models.CharField(max_length=300)),
                ('no_telepon', models.CharField(blank=True, max_length=50, null=True)),
                ('no_hp', models.CharField(blank=True, max_length=50, null=True)),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('modified_by', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('no_hp', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('profil_pic', models.ImageField(blank=True, default='profilepics/avatar.jpeg', null=True, upload_to='profilepics')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TandaTerimaDistribusi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_tanda_terima', models.FileField(blank=True, null=True, upload_to='tanda_terima_distribusi')),
                ('tanggal', models.DateTimeField(auto_now_add=True, null=True)),
                ('lampiran_kontrak', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manajemen_kontrak.lampirankontrak')),
            ],
        ),
        migrations.CreateModel(
            name='PemeriksaanBarang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_pemeriksaan', models.DateField(default=datetime.datetime.now)),
                ('catatan', models.TextField(blank=True, null=True)),
                ('berkas_pemeriksaan', models.FileField(blank=True, null=True, upload_to='berkas_pemeriksaan')),
                ('item_pekerjaan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manajemen_kontrak.lampirankontrak')),
                ('user_pemeriksa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='kontrak',
            name='penyedia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manajemen_kontrak.penyedia'),
        ),
        migrations.CreateModel(
            name='FotoItemPekerjaan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_foto', models.ImageField(blank=True, null=True, upload_to='foto_pekerjaan')),
                ('item_pekerjaan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manajemen_kontrak.lampirankontrak')),
            ],
        ),
    ]