# Generated by Django 3.2.8 on 2021-12-18 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_front', '0002_auto_20211218_0805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationform',
            name='nk_phone_number',
        ),
    ]
