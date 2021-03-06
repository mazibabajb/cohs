# Generated by Django 3.2.8 on 2021-12-18 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(default=0, max_length=30)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('cpd ', 'cpd'), ('diploma', 'diploma'), ('short', 'short')], default='cpd', max_length=30)),
                ('course_thumbnail', models.ImageField(default='default.png', upload_to='cars')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=100)),
                ('course_short_decsrpition', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('iD_Number', models.CharField(max_length=10)),
                ('date_of_bith', models.DateField(auto_now=True)),
                ('physical_address', models.CharField(max_length=300)),
                ('postal_address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField(default=22)),
                ('nk_first_name', models.CharField(max_length=100)),
                ('nk_last_name', models.CharField(max_length=100)),
                ('nk_phone_number', models.IntegerField(default=222)),
                ('course', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='school_front.course')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name', models.CharField(max_length=200)),
                ('module_description', models.TextField(max_length=1000)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_front.course')),
            ],
        ),
    ]
