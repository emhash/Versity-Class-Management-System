# Generated by Django 5.0.1 on 2024-03-10 07:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_initial'),
        ('users', '0007_alter_student_account_alter_teacher_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoutine',
            fields=[
                ('commonbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.commonbasemodel')),
                ('day', models.CharField(choices=[('sat', 'SAT'), ('sun', 'SUN'), ('mon', 'MON'), ('tue', 'TUE'), ('wed', 'WED'), ('thu', 'THU'), ('fri', 'FRI')], max_length=5)),
                ('time', models.CharField(choices=[('08:00AMto09:15AM', '08:00 AM to 09:15 AM'), ('09:15AMto10:30AM', '09:15 AM to 10:30 AM'), ('10:30AMto11:45AM', '10:30 AM to 11:45 AM'), ('11:45AMto01:00PM', '11:45 AM to 01:00 PM'), ('01:30PMto02:45PM', '01:30 PM to 02:45 PM'), ('02:45PMto04:00PM', '02:45 PM to 04:00 PM'), ('04:00PMto05:15PM', '04:00 PM to 05:15 PM'), ('05:15PMto06:30PM', '05:15 PM to 06:30 PM')], max_length=100)),
                ('course_code', models.CharField(max_length=4)),
                ('faculty_short_name', models.CharField(max_length=5)),
                ('building', models.PositiveIntegerField(max_length=3)),
                ('room', models.PositiveIntegerField(max_length=4)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.departments')),
                ('intake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.intakes')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.sections')),
            ],
            options={
                'unique_together': {('day', 'time', 'intake', 'department', 'section')},
            },
            bases=('common.commonbasemodel',),
        ),
    ]
