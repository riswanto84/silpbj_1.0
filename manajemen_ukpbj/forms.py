from django.db.models import fields
from django.forms import ModelForm, widgets
from manajemen_ukpbj.models import *
from django import forms
from django.utils.translation import ugettext_lazy as _

class FormDataSertifikasi(ModelForm):
	class Meta:
		model = PegawaiBersertifikat
		fields = ('nama', 'nip', 'email', 'nomor_hp', 'nomor_sertifikat', 'jenis_sertifikat', 'file_sertifikat', 'foto')

		labels = {
            'foto': _('Foto Profil'),
            'nip': _('NIP'),
            'nama': _('Nama Lengkap'),
            'nomor_hp': _('Nomor HP'),
        }