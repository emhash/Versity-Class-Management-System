# Generated by Django 5.0.1 on 2024-03-09 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_student_gender_alter_teacher_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=50),
        ),
    ]
