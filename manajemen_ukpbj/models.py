from django.db import models
from django.utils import timezone
from datetime import date, datetime

class PegawaiBersertifikat(models.Model):
	CATEGORY = (
		('Tingkat Dasar', 'tingkat dasar'),
		('Standar Kompetensi Level 1', 'kompetensi level 1'),
		('Standar Kompetensi Level 2', 'kompetensi level 2'),
		('Standar Kompetensi Level 3', 'kompetensi level 3'),
		('Lainnya', 'lainnya'),

	)
	nama = models.CharField(max_length=100)
	nip = models.CharField(max_length=18, blank=False)
	email = models.EmailField()
	nomor_hp = models.CharField(max_length=13, blank=True, null=True)
	nomor_sertifikat = models.CharField(max_length=100, blank=True, null=True)
	jenis_sertifikat = models.CharField(max_length=100, choices=CATEGORY, default='Tingkat Dasar')
	file_sertifikat = models.FileField(max_length=255, upload_to='sertifikat_pbj/', blank=True, null=True)
	foto = models.ImageField(default="profilepics/avatar.jpeg", blank=True, null=True, upload_to='profilepics')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nama
