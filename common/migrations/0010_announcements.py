# Generated by Django 5.0.1 on 2024-04-17 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_assignments_date_alter_assignments_types'),
        ('users', '0007_alter_student_account_alter_teacher_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('commonbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.commonbasemodel')),
                ('announcement', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Announcements')),
                ('file', models.FileField(blank=True, null=True, upload_to='Announcements')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.departments')),
                ('intake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.intakes')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.sections')),
                ('who_posted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
            bases=('common.commonbasemodel',),
        ),
    ]