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
 
class FormPaketPengadaan(ModelForm):
    class Meta:
        model = PaketPekerjaan
        fields = '__all__'
        labels = {
            'nama_paket': _('Nama Paket'),
            'nomor_surat_tugas': _('Nomor Surat Tugas'),
            'tanggal_surat_tugas': _('Tanggal Surat Tugas'),
            'file_surat_tugas': _('File Surat Tugas'),
            'nilai_pagu': _('Nilai Pagu'),
            'nilai_hps': _('Nilai HPS'),
            'nilai_hasil_tender': _('Nilai Hasil Tender'),
            'tahun_anggaran': _('Tahun Anggaran'), 
            'dokumen_hps': _('File Dokumen HPS'),
            'dokumen_kak_spek': _('File Dokumen KAK/Spek Teknis'),
            'nomor_surat_usulan_tender': _('Nomor Surat Usulan Tender'),
            'satker_pengguna': _('Satuan Kerja Pengguna/Pemilik Pekerjaan'),
            'tanggal_usulan': _('Tanggal Usulan Tender'),
            'dokumen_surat_usulan': _('File Surat Usulan Tender'),
            'kode_rup': _('Kode RUP'),
            'kode_tender': _('Kode Tender'),
            'pokja_pemilihan': _('Pokja Pemilihan'),
            'status_paket': _('Status Paket'),
            'arsip_dokumen_pengadaan': _('File Arsip Dokumen Pengadaan'),
            
        }