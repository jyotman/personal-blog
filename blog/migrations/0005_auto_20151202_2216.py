# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151104_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
