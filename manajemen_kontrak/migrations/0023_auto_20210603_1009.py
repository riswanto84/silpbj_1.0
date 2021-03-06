# Generated by Django 3.1.1 on 2021-06-03 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0022_auto_20210603_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bagian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_bagian', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='tandaterimadistribusi',
            name='file_tanda_terima',
            field=models.FileField(blank=True, null=True, upload_to='tanda_terima_distribusi'),
        ),
        migrations.AddField(
            model_name='useradmin',
            name='bagian',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manajemen_kontrak.bagian'),
        ),
    ]
