# Generated by Django 4.2.1 on 2023-05-17 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_userprofile_foster_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_foster',
            field=models.BooleanField(default=False),
        ),
    ]
