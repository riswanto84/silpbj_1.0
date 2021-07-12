from django.db import models
from django.utils import timezone
from datetime import date, datetime

class SkPokjaPemilihan(models.Model):
	nomor_sk = models.CharField(max_length=200)
	judul_sk = models.CharField(max_length=250)
	tanggal_sk = models.DateField()
	keterangan = models.TextField(blank=True, null=True)
	file_sk = models.FileField(upload_to='file_sk/', blank=True, null=True)

	def __str__(self):
		return self.nomor_sk

class PegawaiBersertifikat(models.Model):
	CATEGORY = (
		('Tingkat Dasar', 'tingkat dasar'),
		('Standar Kompetensi Level 1', 'kompetensi level 1'),
		('Standar Kompetensi Level 2', 'kompetensi level 2'),
		('Standar Kompetensi Level 3', 'kompetensi level 3'),
		('Lainnya', 'lainnya'),

	)

	STATUS_KEPEG = (
		('Aktif', 'aktif'),
		('Pensiun', 'pensiun')
	)

	TERDAFTAR_POKJA = (
		('Tidak', 'tidak'),
		('Ya', 'ya'),
	)

	nama = models.CharField(max_length=100)
	status_kepegawaian = models.CharField(max_length=100, choices=STATUS_KEPEG, default='Aktif')
	nip = models.CharField(max_length=18, blank=False)
	email = models.EmailField()
	nomor_hp = models.CharField(max_length=13, blank=True, null=True)
	nomor_sertifikat = models.CharField(max_length=100, blank=True, null=True)
	jenis_sertifikat = models.CharField(max_length=100, choices=CATEGORY, default='Tingkat Dasar')
	tanggal_sertifikat = models.DateField(blank=True, null=True)
	file_sertifikat = models.FileField(max_length=255, upload_to='sertifikat_pbj/', blank=True, null=True)
	foto = models.ImageField(default="profilepics/avatar.jpeg", blank=True, null=True, upload_to='profilepics')
	sebagai_pokja_pemilihan = models.CharField(max_length=100, choices=TERDAFTAR_POKJA, default='Tidak')
	sk_pokja = models.ForeignKey(SkPokjaPemilihan, on_delete=models.SET_NULL, null=True, blank=True)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nama

class Satker(models.Model):
	nama_satker = models.CharField(max_length=300)

	def __str__(self):
		return self.nama_satker

class PaketPekerjaan(models.Model):
	STATUS_PAKET = (
		('Persiapan Pengadaan', 'persiapan pengadaan'),
		('Proses Tender', 'proses tender'),
		('Selesai Tender', 'selesai tender'),
	)

	TAHUN_ANGGARAN = (
		('2020', '2020'),
		('2021', '2021'),
		('2022', '2022'),
		('2023', '2023'),
		('2024', '2024'),
		('2025', '2025'),
	)

	tahun = datetime.now().year
    #tahun = tahun_sekarang.year

	nama_paket = models.CharField(max_length=250)
	nomor_surat_tugas = models.CharField(max_length=100)
	tanggal_surat_tugas = models.DateField(blank=False, null=False)
	file_surat_tugas = models.FileField(upload_to='surat_tugas_pokja')
	nilai_pagu = models.FloatField(blank=True, null=True)
	nilai_hps = models.FloatField(blank=True, null=True)
	nilai_hasil_tender = models.FloatField(blank=True, null=True)
	tahun_anggaran = models.CharField(max_length=4, default=tahun, choices=TAHUN_ANGGARAN)
	dokumen_hps =models.FileField(upload_to='dokumen_hps', blank=True, null=True)
	dokumen_kak_spek = models.FileField(upload_to='dokumen_kak_spek', blank=True, null=True)
	nomor_surat_usulan_tender = models.CharField(max_length=200, blank=True, null=True)
	satker_pengguna = models.ForeignKey(Satker, on_delete=models.SET_NULL, null=True, blank=True)
	tanggal_usulan = models.DateField(blank=False, null=False)
	dokumen_surat_usulan = models.FileField(upload_to='dokumen_surat_usulan', blank=True, null=True)
	kode_rup = models.CharField(max_length=10, blank=True, null=True)
	kode_tender = models.CharField(max_length=10, blank=True, null=True)
	pokja_pemilihan = models.ManyToManyField(PegawaiBersertifikat)
	status_paket = models.CharField(max_length=100, choices=STATUS_PAKET, default='Persiapan Pengadaan')
	arsip_dokumen_pengadaan = models.FileField(upload_to='arsip_dokumen_pengadaan', blank=True, null=True)

	def __str__(self):
		return self.nama_paket



