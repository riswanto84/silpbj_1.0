# Generated by Django 3.1.1 on 2021-07-12 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_ukpbj', '0043_paketpekerjaan'),
    ]

    operations = [
        migrations.AddField(
            model_name='paketpekerjaan',
            name='sk_pokja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manajemen_ukpbj.skpokjapemilihan'),
        ),
    ]