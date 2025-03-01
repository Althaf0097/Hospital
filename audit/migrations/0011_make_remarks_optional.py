from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0010_add_patient_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
