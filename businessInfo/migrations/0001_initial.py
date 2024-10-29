# Generated by Django 4.2.13 on 2024-10-14 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('logoDark', models.ImageField(blank=True, null=True, upload_to='business/')),
                ('logoLight', models.ImageField(blank=True, null=True, upload_to='business/')),
                ('aboutUs', models.TextField()),
                ('aboutUsSummary', models.CharField(max_length=1000)),
                ('aboutUsImage', models.ImageField(blank=True, null=True, upload_to='business/')),
                ('tel', models.IntegerField()),
                ('postalCode', models.IntegerField()),
                ('address', models.CharField(max_length=2000)),
                ('email', models.CharField(max_length=500)),
                ('contactUsImage', models.ImageField(blank=True, null=True, upload_to='business/')),
                ('policies', models.TextField()),
                ('policiesImage', models.ImageField(blank=True, null=True, upload_to='business/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
