# Generated by Django 3.1.1 on 2021-07-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_base', '0003_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.ManyToManyField(blank=True, null=True, to='knowledge_base.FilePost'),
        ),
    ]