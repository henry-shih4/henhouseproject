# Generated by Django 4.2.1 on 2023-05-30 04:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0011_alter_petapplication_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='applicants',
            field=models.ManyToManyField(blank=True, related_name='applicants_pets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pet',
            name='interested',
            field=models.ManyToManyField(blank=True, related_name='interested_pets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
