# Generated by Django 5.0.1 on 2025-02-01 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0014_remove_ehcpaudit_abuse_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ehcpaudit',
            name='audit_findings',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
        migrations.AlterField(
            model_name='ehcpaudit',
            name='hnqa_related',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
        migrations.AlterField(
            model_name='ehcpaudit',
            name='other_fraudulent_activities',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
    ]
