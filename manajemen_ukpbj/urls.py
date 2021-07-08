from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('pegawai_bersertifikat/', views.pegawai_bersertifikat, name='pegawai_bersertifikat'),
	
]


