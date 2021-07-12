from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('pegawai_bersertifikat/', views.pegawai_bersertifikat, name='pegawai_bersertifikat'),
	path('detail_pegawai_bersertifikat/<str:pk>', views.detail_pegawai_bersertifikat, name='detail_pegawai_bersertifikat'),
	path('edit_pegawai_bersertifikat/<str:pk>', views.edit_pegawai_bersertifikat, name='edit_pegawai_bersertifikat'),
	path('sk_pokja/', views.sk_pokja, name='sk_pokja'),
	path('paket_pengadaan/<str:tahun>', views.paket_pengadaan, name='paket_pengadaan'),
]


