# Generated by Django 3.2.8 on 2021-12-30 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_front', '0004_remove_registrationform_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_number', models.IntegerField()),
                ('student_name', models.CharField(max_length=100)),
                ('course_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.CharField(choices=[('cpd_training', 'cpd_training'), ('diploma', 'diploma'), ('short', 'short')], default='diploma', max_length=30),
        ),
    ]
