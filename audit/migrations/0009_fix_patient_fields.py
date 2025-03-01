from django.db import migrations, models
import django.core.validators

class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0007_patient_fields_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='deviations',
            field=models.JSONField(default=list, help_text='List of deviations found'),
        ),
    ]
