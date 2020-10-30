# Generated by Django 2.1.7 on 2020-10-20 10:31

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20201019_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150)),
                ('pagepic', models.ImageField(blank=True, null=True, upload_to='')),
                ('about', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=4000)),
                ('aboutpic', models.ImageField(blank=True, null=True, upload_to='')),
                ('top1', models.CharField(blank=True, max_length=150)),
                ('top2', models.CharField(blank=True, max_length=150)),
                ('top3', models.CharField(blank=True, max_length=150)),
                ('top1p', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1000)),
                ('top2p', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1000)),
                ('top3p', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1000)),
                ('meetteam', models.CharField(blank=True, max_length=150)),
                ('teampic1', models.ImageField(blank=True, null=True, upload_to='')),
                ('name1', models.CharField(blank=True, max_length=350)),
                ('role1', models.CharField(blank=True, max_length=350)),
                ('facebook1', models.CharField(blank=True, max_length=750)),
                ('twitter1', models.CharField(blank=True, max_length=750)),
                ('mail1', models.CharField(blank=True, max_length=750)),
                ('instagram1', models.CharField(blank=True, max_length=750)),
                ('description1', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1000)),
                ('teampic2', models.ImageField(blank=True, null=True, upload_to='')),
                ('name2', models.CharField(blank=True, max_length=350)),
                ('role2', models.CharField(blank=True, max_length=350)),
                ('facebook2', models.CharField(blank=True, max_length=750)),
                ('twitter2', models.CharField(blank=True, max_length=750)),
                ('mail2', models.CharField(blank=True, max_length=750)),
                ('instagram2', models.CharField(blank=True, max_length=750)),
                ('description2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1000)),
                ('teampic3', models.ImageField(blank=True, null=True, upload_to='')),
                ('name3', models.CharField(blank=True, max_length=350)),
                ('role3', models.CharField(blank=True, max_length=350)),
                ('facebook3', models.CharField(blank=True, max_length=750)),
                ('twitter3', models.CharField(blank=True, max_length=750)),
                ('mail3', models.CharField(blank=True, max_length=750)),
                ('instagram3', models.CharField(blank=True, max_length=750)),
                ('description3', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1000)),
                ('teampic4', models.ImageField(blank=True, null=True, upload_to='')),
                ('name4', models.CharField(blank=True, max_length=350)),
                ('role4', models.CharField(blank=True, max_length=350)),
                ('facebook4', models.CharField(blank=True, max_length=750)),
                ('twitter4', models.CharField(blank=True, max_length=750)),
                ('mail4', models.CharField(blank=True, max_length=750)),
                ('instagram4', models.CharField(blank=True, max_length=750)),
                ('description4', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1000)),
                ('status', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=150)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='homesetting',
            name='aboutus',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1500),
        ),
        migrations.AlterField(
            model_name='homesetting',
            name='address',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=500),
        ),
    ]
