# Generated by Django 2.1.5 on 2019-01-17 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0006_auto_20190117_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]
