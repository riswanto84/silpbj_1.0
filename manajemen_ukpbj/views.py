from django.shortcuts import render, HttpResponse, redirect
from .models import *
import requests
from django.http import JsonResponse
import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import *

# Create your views here.

@login_required
def pegawai_bersertifikat(request):
	tahun = datetime.now().year
	data_objects = PegawaiBersertifikat.objects.all().order_by('nama')

	form = FormDataSertifikasi

	if request.method == 'POST':
		form = FormDataSertifikasi(request.POST, request.FILES)
		form.save()
		messages.info(request, 'Data berhasildisimpan')
		return redirect('pegawai_bersertifikat')
	context = {
		'tahun': tahun,
		'data_objects': data_objects,
		'form': form,
	}
	return render(request, 'manajemen_ukpbj/pegawai_bersertifikat.html', context)

@login_required
def detail_pegawai_bersertifikat(request, pk):
	tahun = datetime.now().year
	# mendapatkan data pegawai dengan id yang sesuai 
	pegawai = PegawaiBersertifikat.objects.get(id=pk)
	nip = pegawai.nip

	# mendapatkan api kemsos dengan nip 
	api_kemsos = 'https://api-internal.kemensos.go.id/api/pegawai2/' + nip
	response = requests.get(api_kemsos)
	data_pegawai = response.json()
	status_pencarian = data_pegawai['code']
	# jika terdapat data dengan NIP yg sesuai
	if status_pencarian == 404:
		context = {
			'tahun': tahun,
			'data_pegawai': pegawai,
			'nip': pegawai.nip,
		}

	elif status_pencarian ==200:
		context = {
			'tahun': tahun,
			'data_pegawai': pegawai,
			'nama': data_pegawai['data'][0]['nm_peg'],
			'nip': data_pegawai['data'][0]['nip'],
			'npwp': data_pegawai['data'][0]['npwp'],
			'jabatan': data_pegawai['data'][0]['nm_jabatan'],
			'unit_kerja': data_pegawai['data'][0]['UNIT_KERJA'],
			'gelar_preffix': data_pegawai['data'][0]['GELAR_PREFIX'],
			'gelar_suffix': data_pegawai['data'][0]['GELAR_SUFFIX'],

		}
	
	return render(request, 'manajemen_ukpbj/detail_pegawai_bersertifikat.html', context)

@login_required
def edit_pegawai_bersertifikat(request, pk):
	tahun = datetime.now().year
	pegawai = PegawaiBersertifikat.objects.get(id=pk)

	form = FormDataSertifikasi(instance=pegawai)
	if request.method == 'POST':
		form = FormDataSertifikasi(request.POST or None, request.FILES or None, instance=pegawai)
		if form.is_valid():
			form.save()
			messages.info(request, 'Data berhasil diubah')
			return redirect('pegawai_bersertifikat')
	context = {
		'tahun': tahun,
		'form': form,
	}
	return render(request, 'manajemen_ukpbj/edit_pegawai_bersertifikat.html', context)

@login_required
def sk_pokja(request):
	tahun = datetime.now().year
	data_objects = SkPokjaPemilihan.objects.all().order_by('-tanggal_sk')

	form = FormSKPokjamil

	context = {
		'tahun': tahun,
		'data_objects': data_objects,
		'form': form,
	}
	return render(request, 'manajemen_ukpbj/sk_pokja.html', context)

@login_required
def paket_pengadaan(request, tahun):
	if request.method == 'POST':
		tahun = request.POST.get('tahun_anggaran')
		data_objects = PaketPekerjaan.objects.filter(tahun_anggaran=tahun)
		messages.info(request, 'Menampilkan data Tender tahun ' + tahun)

		year_range = []
		tahun_start = 2020
		tahun_end = int(tahun)+1
		while (tahun_start <= tahun_end):
			year_range.append(tahun_start)
			tahun_start = tahun_start + 1

		context = {
			'tahun': tahun,
			'tahun_start': tahun_start,
			'year_range': year_range,
			'data_objects': data_objects,
		}
		return render(request, 'manajemen_ukpbj/paket_pengadaan.html', context)

	tahun = datetime.now().year
	
	year_range = []
	tahun_start = 2020
	tahun_end = tahun
	
	while (tahun_start <= tahun_end):
		year_range.append(tahun_start)
		tahun_start = tahun_start + 1
	
	data_objects = PaketPekerjaan.objects.filter(tahun_anggaran=tahun)

	context = {
		'tahun': tahun,
		'tahun_start': tahun_start,
		'year_range': year_range,
		'data_objects': data_objects,
	}
	return render(request, 'manajemen_ukpbj/paket_pengadaan.html', context)

