# Generated by Django 3.2.13 on 2022-05-20 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_examset_highest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examset',
            name='highest',
        ),
        migrations.AddField(
            model_name='exam',
            name='practice',
            field=models.BooleanField(default=False),
        ),
    ]
