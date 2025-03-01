# Generated by Django 5.0.1 on 2025-01-29 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='EHCPAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_id', models.CharField(max_length=50)),
                ('ehcp_name', models.CharField(max_length=200)),
                ('ehcp_type', models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], max_length=10)),
                ('auditor_name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('current_location', models.CharField(max_length=200)),
                ('visit_date', models.DateField()),
                ('visit_time', models.TimeField()),
                ('ekgp_patients', models.IntegerField(default=0)),
                ('pmjay_patients', models.IntegerField(default=0)),
                ('beneficiaries', models.IntegerField(default=0)),
                ('infrastructure_score', models.IntegerField(default=0)),
                ('service_score', models.IntegerField(default=0)),
                ('documentation_score', models.IntegerField(default=0)),
                ('feedback_score', models.IntegerField(default=0)),
                ('cash_collection', models.BooleanField(default=False)),
                ('medicine_charges', models.BooleanField(default=False)),
                ('falsification', models.BooleanField(default=False)),
                ('other_fraud', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Pending', max_length=20)),
                ('observations', models.TextField(blank=True)),
                ('recommendations', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='audit.district')),
            ],
            options={
                'verbose_name': 'EHCP Audit',
                'verbose_name_plural': 'EHCP Audits',
                'ordering': ['-visit_date', 'ehcp_name'],
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_id', models.CharField(max_length=50)),
                ('patient_name', models.CharField(max_length=200)),
                ('admission_date', models.DateField()),
                ('discharge_date', models.DateField()),
                ('package_name', models.CharField(max_length=200)),
                ('missing_records', models.BooleanField(default=False)),
                ('money_collection', models.BooleanField(default=False)),
                ('remarks', models.TextField(blank=True)),
                ('audit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='audit.ehcpaudit')),
            ],
            options={
                'ordering': ['-admission_date'],
            },
        ),
    ]
