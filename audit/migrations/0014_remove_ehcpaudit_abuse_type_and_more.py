# Generated by Django 5.0.1 on 2025-02-01 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0013_ehcpaudit_abuse_type_ehcpaudit_denial_of_service_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ehcpaudit',
            name='abuse_type',
        ),
        migrations.RemoveField(
            model_name='ehcpaudit',
            name='denial_of_service',
        ),
        migrations.RemoveField(
            model_name='ehcpaudit',
            name='ghost_patient',
        ),
        migrations.RemoveField(
            model_name='ehcpaudit',
            name='has_audit_findings',
        ),
        migrations.RemoveField(
            model_name='ehcpaudit',
            name='has_fraudulent_activities',
        ),
        migrations.RemoveField(
            model_name='ehcpaudit',
            name='has_hnqa_findings',
        ),
        migrations.RemoveField(
            model_name='ehcpaudit',
            name='human_resource_findings',
        ),
        migrations.RemoveField(
            model_name='ehcpaudit',
            name='impersonation',
        ),
        migrations.RemoveField(
            model_name='ehcpaudit',
            name='infrastructure_findings',
        ),
        migrations.RemoveField(
            model_name='ehcpaudit',
            name='oope_type',
        ),
        migrations.RemoveField(
            model_name='ehcpaudit',
            name='opd_to_ipd_conversion',
        ),
        migrations.RemoveField(
            model_name='ehcpaudit',
            name='other_services_findings',
        ),
        migrations.AddField(
            model_name='ehcpaudit',
            name='audit_findings',
            field=models.BooleanField(default=False, verbose_name='Audit Findings'),
        ),
        migrations.AddField(
            model_name='ehcpaudit',
            name='hnqa_related',
            field=models.BooleanField(default=False, verbose_name='HNQA Related'),
        ),
        migrations.AddField(
            model_name='ehcpaudit',
            name='other_fraudulent_activities',
            field=models.BooleanField(default=False, verbose_name='Any Other Fraudulent Activities'),
        ),
    ]
