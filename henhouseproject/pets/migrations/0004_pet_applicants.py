# Generated by Django 4.2.1 on 2023-05-18 18:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_user_is_foster'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='applicants',
            field=models.ManyToManyField(related_name='applicants_pets', to=settings.AUTH_USER_MODEL),
        ),
    ]
