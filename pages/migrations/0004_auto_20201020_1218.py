# Generated by Django 2.1.7 on 2020-10-20 11:18

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20201020_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homesetting',
            name='company',
        ),
        migrations.RemoveField(
            model_name='homesetting',
            name='contactformimg',
        ),
        migrations.AddField(
            model_name='homesetting',
            name='getintouch',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=500),
        ),
    ]
