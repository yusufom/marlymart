# Generated by Django 2.2 on 2020-10-24 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20201024_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagrampost',
            name='title',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
