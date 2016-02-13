# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160123_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
