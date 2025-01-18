# Generated by Django 5.1.5 on 2025-01-18 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0006_alter_program_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramSemester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')])),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semesters', to='academic.program')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semesters', to='academic.academicsession')),
            ],
            options={
                'unique_together': {('program', 'semester', 'session')},
            },
        ),
    ]
