from django.db.models import fields
from django.forms import ModelForm, widgets
from manajemen_ukpbj.models import *
from django import forms
from django.utils.translation import ugettext_lazy as _

class FormDataSertifikasi(ModelForm):
	class Meta:
		model = PegawaiBersertifikat
		fields = ('nama', 'nip', 'status_kepegawaian', 'sebagai_pokja_pemilihan', 'sk_pokja','email', 'nomor_hp', 'nomor_sertifikat', 'tanggal_sertifikat','jenis_sertifikat', 'file_sertifikat', 'foto')

		labels = {
            'foto': _('Foto Profil'),
            'nip': _('NIP'),
            'nama': _('Nama Lengkap'),
            'nomor_hp': _('Nomor HP'),
            'sebagai_pokja_pemilihan': _('Terdaftar Sebagai Pokja'),
            'sk_pokja': _('Nomor SK Pokja'),
        }

class FormSKPokjamil(ModelForm):
    class Meta:
        model = SkPokjaPemilihan
        fields = '__all__'

        labels = {
            'nomor_sk': _('Nomor SK'),
            'judul_sk': _('Judul SK'),
            'tanggal_sk': _('Tanggal SK'),
            'file_sk': _('File SK'),
        }