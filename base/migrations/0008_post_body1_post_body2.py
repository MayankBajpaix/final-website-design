# Generated by Django 4.2.3 on 2023-07-22 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_post_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='body2',
            field=models.TextField(blank=True, null=True),
        ),
    ]
