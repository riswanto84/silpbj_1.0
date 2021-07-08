from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def pegawai_bersertifikat(request):
	tahun = datetime.now().year
	data_objects = PegawaiBersertifikat.objects.all().order_by('nama')

	context = {
		'tahun': tahun,
		'data_objects': data_objects,
	}
	return render(request, 'manajemen_ukpbj/pegawai_bersertifikat.html', context)
