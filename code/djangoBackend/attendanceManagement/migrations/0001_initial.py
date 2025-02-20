# Generated by Django 5.0.1 on 2024-01-27 09:45

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
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=100)),
                ('department_description', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_id', models.AutoField(primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=10)),
                ('age', models.IntegerField()),
                ('contact_address', models.CharField(max_length=200, null=True)),
                ('mobile_number', models.CharField(max_length=100, null=True)),
                ('emp_email', models.EmailField(max_length=254)),
                ('face_state', models.BooleanField(default=False)),
                ('fp_state', models.BooleanField(default=False)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='attendanceManagement.department')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceDetails',
            fields=[
                ('attendance_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('present', models.BooleanField()),
                ('in_time', models.TimeField(null=True)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendanceManagement.employeedetails')),
            ],
        ),
        migrations.CreateModel(
            name='PinData',
            fields=[
                ('pin_id', models.AutoField(primary_key=True, serialize=False)),
                ('pin_code', models.IntegerField(null=True)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendanceManagement.employeedetails')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_id', models.AutoField(primary_key=True, serialize=False)),
                ('MAC', models.GenericIPAddressField(null=True)),
                ('lock_status', models.BooleanField(default=False)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendanceManagement.department')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendanceManagement.topic')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendanceManagement.topic'),
        ),
    ]
