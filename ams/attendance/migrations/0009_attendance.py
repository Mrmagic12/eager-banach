# Generated by Django 4.0.3 on 2022-03-11 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0008_classstudent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_date', models.DateField()),
                ('type', models.CharField(choices=[('1', 'Present'), ('2', 'Tardy'), ('1', 'Absent')], max_length=250)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('classIns', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.student')),
            ],
        ),
    ]