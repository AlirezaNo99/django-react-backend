# Generated by Django 4.2.13 on 2024-05-24 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('status', models.IntegerField()),
                ('keyWords', models.CharField(max_length=330)),
                ('summary', models.CharField(max_length=1000)),
                ('mainPic_base64', models.TextField()),
                ('body_html', models.TextField()),
                ('releaseType', models.IntegerField()),
                ('author_userName', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
            ],
        ),
    ]
