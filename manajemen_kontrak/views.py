from django.contrib.auth.models import Group
from django.db.models.deletion import RestrictedError
from django.shortcuts import render, HttpResponse, redirect, Http404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

from .forms import *
from django.forms import modelformset_factory, inlineformset_factory
from django.core.files.storage import FileSystemStorage
from crispy_forms.helper import FormHelper

from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def under_contructions(request):
    # raise Http404('Under construction')
    return render(request, 'manajemen_kontrak/under_constructions.html')


def master_template(request):
    return render(request, 'manajemen_kontrak/master_template.html')

@csrf_exempt
def login_page(request):
    if request.user.is_authenticated:
        return redirect('home_dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home_dashboard')
            else:
                messages.info(request, 'Username atau Password tidak valid!')
        context = {}
        return render(request, 'manajemen_kontrak/login_page.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login_page')


@login_required(login_url='administrator')
def accountSettings(request):
    user = request.user.useradmin
    form = UserAdminForm(instance=user)
    tahun = datetime.now().year

    if request.method == 'POST':
        form = UserAdminForm(request.POST, request.FILES, instance=user)
        if form.is_valid:
            form.save()
            messages.info(request, 'Data berhasil diubah')

    context = {'form': form, 'tahun': tahun,}
    return render(request, 'manajemen_kontrak/account_settings.html', context)


@login_required(login_url='login_page')
def home_dashboard(request):
    total_barang = Barang.objects.all().count()
    total_penyedia = Penyedia.objects.all().count()
    total_kontrak = Kontrak.objects.all().count()
    tahun = datetime.now().year
    context = {
        'total_barang': total_barang,
        'total_penyedia': total_penyedia,
        'total_kontrak': total_kontrak,
        'tahun': tahun,
    }
    return render(request, 'manajemen_kontrak/MenuDashboardMK.html', context)

# fitur barang


@login_required(login_url='login_page')
def EntryBarang(request):
    form = FormEntryBarang
    data_barang = Barang.objects.all().order_by('-id')
    tahun = datetime.now().year

    if request.method == 'POST':
        form = FormEntryBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil disimpan')
            return redirect('EntryBarang')

    context = {
        'data_barang': data_barang,
        'form': form,
        'tahun': tahun,
    }
    return render(request, 'manajemen_kontrak/FormEntryBarang.html', context)


@login_required(login_url='login_page')
def detail_barang(request, pk):
    detail_barang = Barang.objects.get(id=pk)
    tahun = datetime.now().year
    context = {
        'detail_barang': detail_barang,
        'tahun': tahun,
    }
    return render(request, 'manajemen_kontrak/detail_barang.html', context)

@login_required(login_url='login_page')
def detail_barang_kontrak(request, pk):
    detail_barang = LampiranKontrak.objects.get(id=pk)
    foto = detail_barang.fotoitempekerjaan_set.all()
    log_pemeriksaan = PemeriksaanBarang.objects.filter(item_pekerjaan_id=pk).order_by('-id')

    tahun = datetime.now().year
    context = {
        'detail_barang': detail_barang,
        'tahun': tahun,
        'foto': foto,
        'log_pemeriksaan': log_pemeriksaan,
    }
    return render(request, 'manajemen_kontrak/detail_barang_kontrak.html', context)


@login_required(login_url='login_page')
def ubah_barang(request, pk):
    barang = Barang.objects.get(id=pk)
    form = FormEntryBarang(instance=barang)
    tahun = datetime.now().year

    if request.method == 'POST':
        form = FormEntryBarang(request.POST, instance=barang)
        form.save()
        messages.info(request, 'Data berhasil diubah')
        return redirect('EntryBarang')

    context = {
        'form': form,
        'tahun': tahun,
    }
    return render(request, 'manajemen_kontrak/ubah_barang.html', context)


@login_required(login_url='login_page')
def hapus_barang(request, pk):
    try:
        barang = Barang.objects.get(id=pk)
        barang.delete()
        messages.info(request, 'Data berhasil dihapus')
        return redirect('EntryBarang')
    except RestrictedError:
        return HttpResponse('Tidak dapat menghapus data..!')
# Fitur penyedia


@login_required(login_url='login_page')
def EntryPenyedia(request):
    form = FormEntryPenyedia
    data_penyedia = Penyedia.objects.all().order_by('-id')
    tahun = datetime.now().year

    if request.method == 'POST':
        form = FormEntryPenyedia(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil disimpan')
            return redirect('EntryPenyedia')

    context = {
        'data_penyedia': data_penyedia,
        'form': form,
        'tahun': tahun,
    }
    return render(request, 'manajemen_kontrak/FormEntryPenyedia.html', context)


@login_required(login_url='login_page')
def detail_penyedia(request, pk):
    detail_penyedia = Penyedia.objects.get(id=pk)
    tahun = datetime.now().year
    context = {
        'detail_penyedia': detail_penyedia,
        'tahun': tahun,
    }
    return render(request, 'manajemen_kontrak/detail_penyedia.html', context)


@login_required(login_url='login_page')
def ubah_penyedia(request, pk):
    penyedia = Penyedia.objects.get(id=pk)
    form = FormEntryPenyedia(instance=penyedia)
    tahun = datetime.now().year

    if request.method == 'POST':
        form = FormEntryPenyedia(request.POST, instance=penyedia)
        form.save()
        messages.info(request, 'Data berhasil diubah')
        return redirect('EntryPenyedia')

    context = {
        'form': form,
        'tahun': tahun,
    }
    return render(request, 'manajemen_kontrak/ubah_penyedia.html', context)


@login_required(login_url='login_page')
def hapus_penyedia(request, pk):
    try:
        penyedia = Penyedia.objects.get(id=pk)
        penyedia.delete()
        messages.info(request, 'Data berhasil dihapus')
        return redirect('EntryPenyedia')
    except RestrictedError:
        return HttpResponse('Tidak dapat menghapus data..!')
# Fitur penyedia


@login_required(login_url='login_page')
def EntryKontrak(request, tahun):
    if request.method == 'POST':
        tahun = request.POST.get('tahun_anggaran')
        kontrak = Kontrak.objects.filter(tahun_anggaran=tahun).order_by('-id')
        messages.info(request, 'Menampilkan data kontrak tahun ' + tahun)
        context = {
            'kontrak': kontrak,
            'tahun': tahun,
        }
        return render(request, 'manajemen_kontrak/FormEntryKontrak.html', context)
    tahun = tahun #datetime.now().year
    kontrak = Kontrak.objects.filter(tahun_anggaran=tahun).order_by('-id')
    context = {'kontrak': kontrak, 'tahun': tahun}
    return render(request, 'manajemen_kontrak/FormEntryKontrak.html', context)


@login_required(login_url='login_page')
def TambahKontrak(request):
    form = FormEntryKontrak
    tahun = datetime.now().year
    if request.method == 'POST':
        form = FormEntryKontrak(request.POST, request.FILES)
        # tahun = request.POST.get('tahun_anggaran')
        if form.is_valid():
            form.save()
            messages.info(request, 'Data kontrak berhasil disimpan')
            return redirect('EntryKontrak', tahun=request.POST.get('tahun_anggaran'))

    context = {
        'form': form,
        'tahun': tahun
    }
    return render(request, 'manajemen_kontrak/FormTambahKontrak.html', context)


@login_required(login_url='login_page')
def DetailKontrak(request, pk):
    detail_kontrak = Kontrak.objects.get(id=pk)
    item_barang = detail_kontrak.lampirankontrak_set.all()
    data_barang = Barang.objects.all()
    tahun = datetime.now().year
    form = FormLampiranKontrak
    formubah = FormLampiranKontrak

    tahun_anggaran = detail_kontrak.tahun_anggaran

    if request.method == 'POST':
        # return HttpResponse('id_kontrak')
        nomor_kontrak_id = request.POST.get('nomor_kontrak_id')
        barang_id = request.POST.get('barang')
        kuantitas = request.POST.get('kuantitas')
        harga_satuan = request.POST.get('harga_satuan')
        created_by = request.POST.get('created_by')
        #return HttpResponse(created_by)
        data = LampiranKontrak(
            nomor_kontrak_id=nomor_kontrak_id,
            barang_id=barang_id,
            kuantitas=kuantitas,
            harga_satuan=harga_satuan,
            created_by=created_by,
        )
        data.save()
        messages.info(request, 'Data berhasil disimpan')

    context = {
        'detail_kontrak': detail_kontrak,
        'item_barang': item_barang,
        'tahun': tahun_anggaran,
        'form': form,
        'formubah': formubah,
    }
    return render(request, 'manajemen_kontrak/detail_kontrak.html', context)


@ login_required
def hapus_detail_kontrak(request, pk):
    # return HttpResponse("Hapus")
    try:
        detail_kontrak = LampiranKontrak.objects.get(id=pk)
        id_kontrak = detail_kontrak.nomor_kontrak.id
        detail_kontrak.delete()
        messages.info(request, 'Data berhasil dihapus')
        return redirect('DetailKontrak', pk=id_kontrak)

    except RestrictedError:
        return HttpResponse('Tidak dapat menghapus data..!')


@login_required(login_url='login_page')
def ubah_kontrak(request, pk):
    kontrak = Kontrak.objects.get(id=pk)
    form = FormEntryKontrak(instance=kontrak)
    tahun_anggaran = kontrak.tahun_anggaran

    if request.method == 'POST':
        form = FormEntryKontrak(request.POST, request.FILES, instance=kontrak)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil diubah')
            return redirect('EntryKontrak', tahun=tahun_anggaran)

    context = {'form': form, 'tahun': tahun_anggaran}
    return render(request, 'manajemen_kontrak/FormUbahKontrak.html', context)


@login_required(login_url='login_page')
def hapus_kontrak(request, pk):
    kontrak = Kontrak.objects.get(id=pk)
    tahun_anggaran = kontrak.tahun_anggaran
    kontrak.delete()
    messages.info(request, 'Kontrak berhasil dihapus')
    return redirect('EntryKontrak', tahun=tahun_anggaran)


@login_required(login_url='login_page')
def tambah_lampiran_kontrak(request, pk):
    kontrak = Kontrak.objects.get(id=pk)
    LampiranKontrakFormset = inlineformset_factory(
        Kontrak, LampiranKontrak, fields=('barang', 'kuantitas', 'harga_satuan',), extra=5, can_delete=False)
    item_barang = kontrak.lampirankontrak_set.all()
    images = request.FILES.getlist('images')
    tahun_anggaran = kontrak.tahun_anggaran

    if request.method == 'POST':
        formset = LampiranKontrakFormset(
            request.POST, request.FILES, instance=kontrak)
        if formset.is_valid():
            formset.save()
            messages.info(request, 'Data berhasil disimpan')
            context = {
                'detail_kontrak': kontrak,
                'item_barang': item_barang,
            }
            return redirect('DetailKontrak', pk=pk)

    formset = LampiranKontrakFormset(instance=kontrak)
    context = {
        'formset': formset,
        'id': pk,
        'kontrak': kontrak,
        'tahun': tahun_anggaran,
    }
    return render(request, 'manajemen_kontrak/tambah_barang_kontrak.html', context)

    # return HttpResponse('tes')


@login_required
def ubah_detil_rab(request, pk):
    detil_rab = LampiranKontrak.objects.get(id=pk)
    kontrak = Kontrak.objects.get(id=detil_rab.nomor_kontrak_id)
    form = FormUbahLampiranKontrak(instance=detil_rab)
    tahun_anggaran = kontrak.tahun_anggaran

    if request.method == 'POST':
        kontrak_pk = request.POST.get('kontrak_pk')
        form = FormUbahLampiranKontrak(request.POST, instance=detil_rab)
        form.save()
        messages.info(request, 'Data berhasil diubah')
        return redirect('DetailKontrak', pk=kontrak_pk)

    context = {
        'form': form,
        'detil_rab': detil_rab,
        'id': pk,
        'tahun': tahun_anggaran,
    }
    return render(request, 'manajemen_kontrak/ubah_detil_rab.html', context)


@login_required(login_url='login_page')
def foto_item_pekerjaan(request, pk):
    lampirankontrak = LampiranKontrak.objects.get(id=pk)
    FotoPekerjaanFormset = inlineformset_factory(
        LampiranKontrak, FotoItemPekerjaan, fields=('file_foto',), can_delete=False)
    item_foto = lampirankontrak.fotoitempekerjaan_set.all()
    images = lampirankontrak.fotoitempekerjaan_set.all()
    id_kontrak = lampirankontrak.nomor_kontrak.id

    if request.method == 'POST':
        formset = FotoPekerjaanFormset(
            request.POST, request.FILES, instance=lampirankontrak)
        if formset.is_valid():
            formset.save()
            messages.info(request, 'Data berhasil disimpan')
            # return redirect('DetailKontrak', pk=id_kontrak)

    formset = FotoPekerjaanFormset(instance=lampirankontrak)
    tahun = datetime.now().year
    context = {
        'formset': formset,
        'tahun': tahun,
        'lampirankontrak': lampirankontrak,
        'images': images,
    }

    return render(request, 'manajemen_kontrak/foto_pekerjaan.html', context)


@login_required(login_url='login_page')
def tanda_terima_distribusi(request, pk):
    lampirankontrak = LampiranKontrak.objects.get(id=pk)
    tandaTerimaFormset = inlineformset_factory(
        LampiranKontrak, TandaTerimaDistribusi, fields=('file_tanda_terima',), can_delete=False)
    id_kontrak = lampirankontrak.nomor_kontrak.id

    if request.method == 'POST':
        formset = tandaTerimaFormset(
            request.POST, request.FILES, instance=lampirankontrak)
        if formset.is_valid():
            formset.save()
            messages.info(request, 'Data berhasil disimpan')
            # return redirect('DetailKontrak', pk=id_kontrak)

    formset = tandaTerimaFormset(instance=lampirankontrak)
    tahun = datetime.now().year
    files = lampirankontrak.tandaterimadistribusi_set.all()

    context = {
        'formset': formset,
        'tahun': tahun,
        'lampirankontrak': lampirankontrak,
    }

    return render(request, 'manajemen_kontrak/tanda_terima.html', context)

@login_required
def pemeriksaan_pekerjaan(request, pk):
    lampirankontrak = LampiranKontrak.objects.get(id=pk)
    form = FormPemeriksaanBarang(initial={'item_pekerjaan': lampirankontrak})
    log_pemeriksaan = PemeriksaanBarang.objects.filter(item_pekerjaan_id=pk).order_by('-id')

    if request.method == 'POST':
        form = FormPemeriksaanBarang(request.POST, request.FILES)
        if form.is_valid():
            print(request.POST, request.FILES)
            form.save()
            messages.info(request, 'Data berhasil disimpan')
            return redirect('pemeriksaan_pekerjaan', pk)
    
    tahun = datetime.now().year
    context = {
        'form': form,
        'tahun': tahun,
        'lampirankontrak': lampirankontrak,
        'log_pemeriksaan': log_pemeriksaan,
    }
    return render(request, 'manajemen_kontrak/pemeriksaan.html', context)

@login_required
def hapus_catatan_pemeriksaaan(request, pk):
    #return HttpResponse('Hapus')
    catatan_pemeriksaan = PemeriksaanBarang.objects.get(id=pk)
    catatan_pemeriksaan.delete()
    messages.info(request, 'Data berhasil dihapus')
    return redirect('pemeriksaan_pekerjaan', catatan_pemeriksaan.item_pekerjaan_id)
