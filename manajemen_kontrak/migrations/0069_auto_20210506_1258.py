# Generated by Django 3.1.1 on 2021-05-06 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0068_auto_20210505_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='lampirankontrak',
            name='created_by',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='lampirankontrak',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='lampirankontrak',
            name='modified_by',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='lampirankontrak',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='tandaterimadistribusi',
            name='nomor_tanda_terima',
            field=models.CharField(default='4561/jxZsz2Mw', max_length=100),
        ),
    ]
