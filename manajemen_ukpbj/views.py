from django.shortcuts import render, HttpResponse, redirect
from .models import *
import requests
from django.http import JsonResponse
import json
from django.contrib import messages

from .forms import *

# Create your views here.

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

def detail_pegawai_bersertifikat(request, pk):
	tahun = datetime.now().year
	# mendapatkan data pegawai dengan id yang sesuai 
	pegawai = PegawaiBersertifikat.objects.get(id=pk)
	nip = pegawai.nip

	# mendapatkan api kemsos dengan nip 
	api_kemsos = 'https://api-internal.kemensos.go.id/api/pegawai2/' + nip
	response = requests.get(api_kemsos)
	data_pegawai = response.json()
	
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
