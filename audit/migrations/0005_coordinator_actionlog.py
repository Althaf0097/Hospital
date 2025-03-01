# Generated by Django 5.0.1 on 2025-01-31 08:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0004_rename_has_package_patient_missing_records_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('employee_id', models.CharField(max_length=20, unique=True)),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='audit.district')),
            ],
            options={
                'verbose_name': 'Coordinator',
                'verbose_name_plural': 'Coordinators',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ActionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_type', models.CharField(choices=[('AUDIT', 'Audit Performed'), ('PATIENT_UPDATE', 'Patient Details Updated'), ('RECORD_CHECK', 'Records Checked'), ('MONEY_VERIFY', 'Money Status Verified'), ('OTHER', 'Other Action')], max_length=20)),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='completed', max_length=20)),
                ('notes', models.TextField(blank=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.district')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='audit.patient')),
                ('coordinator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.coordinator')),
            ],
            options={
                'verbose_name': 'Action Log',
                'verbose_name_plural': 'Action Logs',
                'ordering': ['-timestamp'],
            },
        ),
    ]
