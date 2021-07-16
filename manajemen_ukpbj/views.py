from django.shortcuts import render, HttpResponse, redirect
from .models import *
import requests
from django.http import JsonResponse
import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import *

# Library PyProc
from pyproc import Lpse


@login_required(login_url='login_page')
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

@login_required(login_url='login_page')
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

@login_required(login_url='login_page')
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

@login_required(login_url='login_page')
def paket_pengadaan(request, tahun):
	if request.method == 'POST':
		tahun = request.POST.get('tahun_anggaran')
		data_objects = PaketPekerjaan.objects.filter(tahun_anggaran=tahun).order_by('-tanggal_surat_tugas')
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
	
	data_objects = PaketPekerjaan.objects.filter(tahun_anggaran=tahun).order_by('-tanggal_surat_tugas')

	context = {
		'tahun': tahun,
		'tahun_start': tahun_start,
		'year_range': year_range,
		'data_objects': data_objects,
	}
	return render(request, 'manajemen_ukpbj/paket_pengadaan.html', context)

@login_required(login_url='login_page')
def buat_paket_pengadaan(request):
	tahun = datetime.now().year
	form = FormPaketPengadaan
	if request.method == 'POST':
		form = FormPaketPengadaan(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.info(request, 'Data paket pengadaan berhasil disimpan')
			return redirect('paket_pengadaan', tahun=request.POST.get('tahun_anggaran'))
	context = {
		'tahun': tahun,
		'form': form,
	}
	return render(request, 'manajemen_ukpbj/buat_paket_pengadaan.html', context)

@login_required(login_url='login_page')
def edit_paket_pengadaan(request, pk):
	tahun = datetime.now().year
	data_objects = PaketPekerjaan.objects.get(id=pk)
	
	form = FormPaketPengadaan(instance=data_objects)
	if request.method == 'POST':
		form = FormPaketPengadaan(request.POST or None, request.FILES or None, instance=data_objects)
		if form.is_valid():
			form.save()
			messages.info(request, 'Data berhasil diubah')
			return redirect('paket_pengadaan', tahun=tahun)
	context = {
		'tahun': tahun,
		'form': form,
	}
	return render(request, 'manajemen_ukpbj/edit_paket_pengadaan.html', context)

@login_required(login_url='login_page')
def detail_paket_pengadaan(request, pk):
	tahun = datetime.now().year
	data_objects = PaketPekerjaan.objects.get(id=pk)

	# Inisiasi objek lpse kementerian keuangan
	lpse = Lpse('http://lpse.kemenkeu.go.id')
	id_paket = data_objects.kode_tender

	if id_paket is not None:
		detil = lpse.detil_paket_tender(id_paket=id_paket)
		# mendapatkan link tender LPSE
		link_tender = 'https://lpse.kemenkeu.go.id/eproc4/lelang/' + id_paket + '/pengumumanlelang'
		# mendapatkan hanya pemenang lelang
		pemenang = detil.get_pemenang()
		json_pemenang = json.dumps(pemenang)
		data_json = json.loads(json_pemenang)

		context = {
			'tahun': tahun,
			'data_objects': data_objects,
			'lpse': lpse,
			'detil': detil,
			'link_tender': link_tender,
			'json_pemenang': json_pemenang,
			'data_json': data_json,
		}
		return render(request, 'manajemen_ukpbj/detail_paket_pengadaan.html', context)
	
	else:
		context = {
			'tahun': tahun,
			'data_objects': data_objects,
		}

		return render(request, 'manajemen_ukpbj/detail_paket_pengadaan.html', context)
