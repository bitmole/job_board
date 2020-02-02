# Generated by Django 3.0.2 on 2020-02-02 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=60)),
                ('company_email', models.EmailField(max_length=254)),
                ('job_title', models.CharField(max_length=60)),
                ('job_description', models.TextField(blank=True)),
                ('salary', models.IntegerField()),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
