# Generated by Django 4.2.1 on 2023-05-19 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0007_petapplication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petapplication',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='petapplication',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]