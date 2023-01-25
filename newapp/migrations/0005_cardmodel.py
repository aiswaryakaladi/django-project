# Generated by Django 4.1.3 on 2022-11-16 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_filemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='cardmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('image', models.FileField(upload_to='newapp/static')),
                ('description', models.CharField(max_length=60)),
            ],
        ),
    ]
