# Generated by Django 2.2.11 on 2020-08-05 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facility', '0152_auto_20200805_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalpatientregistration',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='patientregistration',
            name='assigned_to',
        ),
        migrations.AddField(
            model_name='historicalpatientregistration',
            name='last_consultation',
            field=models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='facility.PatientConsultation'),
        ),
        migrations.AddField(
            model_name='patientconsultation',
            name='assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient_assigned_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='patientregistration',
            name='last_consultation',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='facility.PatientConsultation'),
        ),
    ]