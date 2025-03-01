from django.db import migrations, models
import django.core.validators

class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0006_coordinator_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='mobile_number',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='package_code',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='deviations',
            field=models.JSONField(default=list, help_text='List of deviations found'),
        ),
        migrations.AddField(
            model_name='patient',
            name='total_oope',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Total Out of Pocket Expenses'),
        ),
        migrations.AddField(
            model_name='patient',
            name='case_file',
            field=models.FileField(blank=True, null=True, upload_to='case_files/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png', 'doc', 'docx'])], verbose_name='Case File'),
        ),
        migrations.AddField(
            model_name='patient',
            name='discharge_summary',
            field=models.FileField(blank=True, null=True, upload_to='discharge_summaries/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png', 'doc', 'docx'])]),
        ),
        migrations.AddField(
            model_name='patient',
            name='bills_documents',
            field=models.FileField(blank=True, null=True, upload_to='bills/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])], verbose_name='Bills and Documents'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='case_id',
            field=models.CharField(max_length=100, unique=True, verbose_name='Case ID / IP Number'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='discharge_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='case_summary',
            field=models.TextField(blank=True),
        ),
    ]
