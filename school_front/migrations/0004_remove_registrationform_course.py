# Generated by Django 3.2.8 on 2021-12-18 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_front', '0003_remove_registrationform_nk_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationform',
            name='course',
        ),
    ]
