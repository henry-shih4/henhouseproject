# Generated by Django 4.2.1 on 2023-05-19 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0009_alter_pet_applicants_alter_pet_interested'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petapplication',
            name='email',
        ),
    ]
