from os import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('master_template/', views.master_template, name='master_template'),
    path('under_contructions/', views.under_contructions,
         name='under_contructions'),

    # path untuk login admin
    path('', views.login_page, name='login_page'),
    path('logout/', views.logoutUser, name='logout'),
    path('home_dashboard/', views.home_dashboard, name='home_dashboard'),
    path('account_setting/', views.accountSettings, name='account_setting'),

    # path untuk use case entry barang
    path('EntryBarang/', views.EntryBarang, name='EntryBarang'),
    path('detail_barang/<str:pk>', views.detail_barang, name='detail_barang'),
    path('ubah_barang/<str:pk>', views.ubah_barang, name='ubah_barang'),
    path('hapus_barang/<str:pk>', views.hapus_barang, name='hapus_barang'),

    # path untuk use case entry penyedia
    path('EntryPenyedia/', views.EntryPenyedia, name='EntryPenyedia'),
    path('detail_penyedia/<str:pk>', views.detail_penyedia, name='detail_penyedia'),
    path('ubah_penyedia/<str:pk>', views.ubah_penyedia, name='ubah_penyedia'),
    path('hapus_penyedia/<str:pk>', views.hapus_penyedia, name='hapus_penyedia'),

    # path untuk use case entry kontrak
    path('EntryKontrak/<str:tahun>', views.EntryKontrak, name='EntryKontrak'),
    path('TambahKontrak', views.TambahKontrak, name='TambahKontrak'),
    path('DetailKontrak/<str:pk>', views.DetailKontrak, name='DetailKontrak'),
    path('hapus_detail_kontrak/<str:pk>',
         views.hapus_detail_kontrak, name='hapus_detail_kontrak'),
    path('HapusKontrak/<str:pk>',
         views.hapus_kontrak, name='hapus_kontrak'),
    path('ubah_kontrak/<str:pk>', views.ubah_kontrak, name='ubah_kontrak'),
    path('tambah_lampiran_kontrak/<str:pk>',
         views.tambah_lampiran_kontrak, name='tambah_lampiran_kontrak'),
    path('ubah_detil_rab/<str:pk>', views.ubah_detil_rab, name='ubah_detil_rab'),
    path('foto_item_pekerjaan/<str:pk>',
         views.foto_item_pekerjaan, name='foto_item_pekerjaan'),
    path('tanda_terima_distribusi/<str:pk>',
         views.tanda_terima_distribusi, name='tanda_terima_distribusi'),
    path('pemeriksaan_pekerjaan/<str:pk>', views.pemeriksaan_pekerjaan, name='pemeriksaan_pekerjaan'),


    # path untuk reset password
    path('reset_password/', auth_views.PasswordResetView.as_view(),
         name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
