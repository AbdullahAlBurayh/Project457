# Generated by Django 3.2.13 on 2022-05-20 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20220521_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='questions',
            field=models.ManyToManyField(to='exam.Question'),
        ),
    ]