# Generated by Django 2.1.5 on 2019-01-17 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0007_auto_20190117_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
