# Generated by Django 2.2.5 on 2019-10-29 18:06

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20191007_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apt_building',
            name='amount_of_user',
        ),
        migrations.RemoveField(
            model_name='bike_video',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='bike_video',
            name='time_update',
        ),
        migrations.RemoveField(
            model_name='toolbox',
            name='video',
        ),
        migrations.AddField(
            model_name='bike_video',
            name='tiem_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='bike_video',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 10, 29, 18, 6, 37, 494810, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apt_building',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.RemoveField(
            model_name='tool',
            name='toolbox',
        ),
        migrations.AddField(
            model_name='tool',
            name='toolbox',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.toolbox'),
        ),
        migrations.RemoveField(
            model_name='toolbox',
            name='building',
        ),
        migrations.AddField(
            model_name='toolbox',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.apt_building'),
        ),
        migrations.AlterField(
            model_name='toolbox',
            name='sponsor',
            field=models.ManyToManyField(to='database.bike_company'),
        ),
        migrations.AlterField(
            model_name='toolbox',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.RemoveField(
            model_name='toolbox',
            name='user_rent',
        ),
        migrations.AddField(
            model_name='toolbox',
            name='user_rent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.user'),
        ),
    ]
