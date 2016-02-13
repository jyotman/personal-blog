# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160117_0144'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Visits',
            new_name='Visit',
        ),
    ]
