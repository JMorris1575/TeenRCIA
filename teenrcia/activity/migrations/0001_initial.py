# Generated by Django 2.1.5 on 2019-01-14 02:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.SmallIntegerField(unique=True)),
                ('title', models.CharField(max_length=100)),
                ('overview', models.CharField(blank=True, max_length=512)),
                ('publish_date', models.DateField(null=True)),
                ('open', models.BooleanField(default=True)),
                ('archive', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'activities',
                'ordering': ['index'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('comment_date_time', models.DateTimeField()),
            ],
            options={
                'ordering': ['comment_date_time'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.SmallIntegerField()),
                ('text', models.CharField(max_length=512)),
            ],
            options={
                'ordering': ['index'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('post_date_time', models.DateTimeField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['post_date_time'],
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.SmallIntegerField()),
                ('instructions', models.CharField(max_length=512)),
                ('link_name', models.CharField(blank=True, max_length=50)),
                ('link', models.URLField(blank=True, default='')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Activity')),
            ],
            options={
                'ordering': ['index'],
            },
        ),
        migrations.AddField(
            model_name='item',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Section'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together={('activity', 'index')},
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('section', 'index')},
        ),
    ]