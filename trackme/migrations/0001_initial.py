# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=20)),
                ('reports', models.IntegerField(default=0)),
                ('profilePicture', models.ImageField(upload_to=b'trackme/profilePictures')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
