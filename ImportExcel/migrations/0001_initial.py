# Generated by Django 4.0.1 on 2022-01-20 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_file', models.FileField(upload_to='')),
                ('file_name', models.CharField(default='', max_length=120)),
                ('date_upload', models.DateTimeField(auto_now_add=True)),
                ('date_processed', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(default='loaded', max_length=120)),
                ('results', models.CharField(default='', max_length=120)),
            ],
        ),
    ]
