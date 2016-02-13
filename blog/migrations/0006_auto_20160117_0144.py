# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20151202_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visits',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('post', models.BooleanField()),
                ('name', models.CharField(unique=True, max_length=100)),
                ('count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='visits',
            field=models.ForeignKey(to='blog.Visits', default=0),
            preserve_default=False,
        ),
    ]
