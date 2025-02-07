# Generated by Django 5.1.5 on 2025-01-18 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('faculty', models.CharField(choices=[('E&t', 'Engineering AND Technology'), ('i&c', 'Informatic AND computing'), ('Sc', 'Science'), ('MAGT', 'Management'), ('MS', 'Media Studies'), ('LS', 'Life Sciences'), ('IS', 'Intrdisciplinary Studies'), ('CCSD', 'Community College for Skill Development'), ('OTHER', 'Others')], default='OTHER', max_length=10)),
            ],
        ),
    ]
