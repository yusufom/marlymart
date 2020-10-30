# Generated by Django 2.1.7 on 2020-10-19 11:27

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150)),
                ('keywords', models.CharField(blank=True, max_length=150)),
                ('description', models.CharField(blank=True, max_length=150)),
                ('company', models.CharField(blank=True, max_length=150)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('phone', models.CharField(blank=True, max_length=150)),
                ('black_quote', models.CharField(blank=True, max_length=150)),
                ('headline2', models.CharField(blank=True, max_length=150)),
                ('head2Qwords', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=500)),
                ('headline3', models.CharField(blank=True, max_length=150)),
                ('head3Qwords', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=500)),
                ('question', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=200)),
                ('buyer', models.CharField(blank=True, max_length=150)),
                ('seller', models.CharField(blank=True, max_length=150)),
                ('aim', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1500)),
                ('whatWeDo', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1500)),
                ('popularQuote', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=500)),
                ('quoter', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=150)),
                ('email', models.CharField(blank=True, max_length=150)),
                ('smtpserver', models.CharField(blank=True, max_length=150)),
                ('smtpemail', models.CharField(blank=True, max_length=150)),
                ('smtppassword', models.CharField(blank=True, max_length=150)),
                ('smtpport', models.CharField(blank=True, max_length=150)),
                ('icon', models.ImageField(blank=True, max_length=150, upload_to='')),
                ('facebook', models.CharField(blank=True, max_length=150)),
                ('instagram', models.CharField(blank=True, max_length=150)),
                ('twitter', models.CharField(blank=True, max_length=150)),
                ('aboutus', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=150)),
                ('contact', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=150)),
                ('refrences', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=150)),
                ('status', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=150)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
