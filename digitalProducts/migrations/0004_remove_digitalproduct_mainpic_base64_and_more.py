# Generated by Django 4.2.13 on 2024-09-14 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalProducts', '0003_digitalproduct_mainpicalt_digitalproduct_productlink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='digitalproduct',
            name='mainPic_base64',
        ),
        migrations.AddField(
            model_name='digitalproduct',
            name='mainPic',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
