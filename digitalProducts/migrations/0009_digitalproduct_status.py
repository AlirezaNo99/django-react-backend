# Generated by Django 4.2.13 on 2025-01-14 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalProducts', '0008_remove_digitalproduct_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='digitalproduct',
            name='status',
            field=models.IntegerField(default=2),
        ),
    ]