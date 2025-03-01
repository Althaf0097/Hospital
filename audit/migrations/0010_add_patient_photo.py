from django.db import migrations, models
import django.core.validators

class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0009_fix_patient_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='patient_photo',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='patient_photos/%Y/%m/%d/',
                validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
                verbose_name='Patient Photo'
            ),
        ),
    ]
