# Generated by Django 5.1.6 on 2025-02-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0023_ehcpaudit_abuse_ehcpaudit_abuse_details_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ehcpaudit',
            name='abuse',
        ),
        migrations.RemoveField(
            model_name='ehcpaudit',
            name='abuse_details',
        ),
        migrations.RemoveField(
            model_name='ehcpaudit',
            name='audit_findings',
        ),
        migrations.RemoveField(
            model_name='ehcpaudit',
            name='denial_details',
        ),
        migrations.RemoveField(
            model_name='ehcpaudit',
            name='denial_of_service',
        ),
        migrations.RemoveField(
            model_name='ehcpaudit',
            name='oope',
        ),
        migrations.RemoveField(
            model_name='ehcpaudit',
            name='oope_details',
        ),
        migrations.AddField(
            model_name='ehcpaudit',
            name='abuse_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ehcpaudit',
            name='audit_findings_value',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='ehcpaudit',
            name='finding_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ehcpaudit',
            name='findings_type',
            field=models.CharField(blank=True, choices=[('audit_findings', 'AUDIT FINDINGS'), ('hnqa_related', 'HNQA RELATED'), ('other_fraudulent_activities', 'ANY OTHER FRAUDULENT ACTIVITIES')], default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ehcpaudit',
            name='fraudulent_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ehcpaudit',
            name='fraudulent_value',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='ehcpaudit',
            name='hnqa_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ehcpaudit',
            name='hnqa_value',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='ehcpaudit',
            name='hr_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ehcpaudit',
            name='infrastructure_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ehcpaudit',
            name='oope_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ehcpaudit',
            name='photos',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ehcpaudit',
            name='services_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ehcpaudit',
            name='signature',
            field=models.TextField(blank=True, null=True),
        ),
    ]
