# Generated by Django 3.1.1 on 2021-07-12 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_ukpbj', '0011_delete_pokjapemilihan'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkPokjaPemilihan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul_sk', models.CharField(max_length=250)),
                ('tanggal_sk', models.DateField(auto_now=True)),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='pegawaibersertifikat',
            name='sebagai_pokja_pemilihan',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pegawaibersertifikat',
            name='sk_pokja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manajemen_ukpbj.skpokjapemilihan'),
        ),
    ]