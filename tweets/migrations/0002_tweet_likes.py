# Generated by Django 2.2 on 2021-10-27 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='likes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
