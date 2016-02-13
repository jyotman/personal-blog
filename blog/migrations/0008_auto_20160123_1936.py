# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160123_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='count',
            new_name='dailyCount',
        ),
        migrations.AddField(
            model_name='visit',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 1, 23, 14, 6, 25, 82307, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visit',
            name='totalCount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
