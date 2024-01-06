# Generated by Django 5.0 on 2024-01-06 03:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dep_id', models.AutoField(primary_key=True, serialize=False)),
                ('dep_name', models.CharField(max_length=100)),
                ('no_emp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=10)),
                ('age', models.IntegerField()),
                ('contact_address', models.CharField(max_length=200)),
                ('emp_email', models.EmailField(max_length=254)),
                ('emp_password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_id', models.AutoField(primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=50)),
                ('dev_connected', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Attendance_Details',
            fields=[
                ('attendance_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('present', models.BooleanField()),
                ('in_time', models.TimeField()),
                ('out_time', models.TimeField()),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendanceManagement.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Job_Title',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('dep_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendanceManagement.department')),
            ],
        ),
        migrations.CreateModel(
            name='Duty_Duration',
            fields=[
                ('duty_id', models.AutoField(primary_key=True, serialize=False)),
                ('duration', models.IntegerField()),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendanceManagement.employee')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendanceManagement.job_title')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='topic_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendanceManagement.topic'),
        ),
    ]
