# Generated by Django 2.1 on 2019-12-09 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Latest_results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('channel_Title', models.CharField(max_length=100)),
                ('date_published', models.DateTimeField(max_length=100)),
            ],
        ),
    ]
