# Generated by Django 4.2.3 on 2023-07-22 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_post_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
    ]
