# Generated by Django 3.2.16 on 2023-01-06 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='featred_image',
            new_name='featured_image',
        ),
    ]
