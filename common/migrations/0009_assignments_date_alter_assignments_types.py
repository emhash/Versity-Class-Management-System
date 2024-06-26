# Generated by Django 5.0.1 on 2024-04-16 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_assignments_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignments',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='assignments',
            name='types',
            field=models.CharField(choices=[('assignment', 'Assignment'), ('lab_report', 'Lab Report'), ('presentation', 'Peresentation')], default='assignment', max_length=50),
        ),
    ]
