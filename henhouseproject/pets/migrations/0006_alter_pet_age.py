# Generated by Django 4.2.1 on 2023-05-18 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0005_userprofile_age_userprofile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
