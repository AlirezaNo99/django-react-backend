# Generated by Django 4.2.13 on 2024-10-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessInfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessinfo',
            name='Banner1',
            field=models.ImageField(blank=True, null=True, upload_to='business/'),
        ),
        migrations.AddField(
            model_name='businessinfo',
            name='Banner2',
            field=models.ImageField(blank=True, null=True, upload_to='business/'),
        ),
        migrations.AddField(
            model_name='businessinfo',
            name='Banner3',
            field=models.ImageField(blank=True, null=True, upload_to='business/'),
        ),
        migrations.AddField(
            model_name='businessinfo',
            name='mainBanner',
            field=models.ImageField(blank=True, null=True, upload_to='business/'),
        ),
    ]