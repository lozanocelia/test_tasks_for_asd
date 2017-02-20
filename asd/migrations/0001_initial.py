# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 06:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Filename',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filenames', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('checksum', models.CharField(max_length=32)),
                ('users', models.ManyToManyField(related_name='uploaded_files', through='asd.Filename', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='filename',
            name='uploaded_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filenames', to='asd.UploadedFile'),
        ),
    ]