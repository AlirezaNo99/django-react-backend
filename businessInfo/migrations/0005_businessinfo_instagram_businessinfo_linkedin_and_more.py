# Generated by Django 4.2.13 on 2024-12-15 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessInfo', '0004_businessinfo_banner4_businessinfo_banner4link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessinfo',
            name='Instagram',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='businessinfo',
            name='Linkedin',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='businessinfo',
            name='Telegram',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
