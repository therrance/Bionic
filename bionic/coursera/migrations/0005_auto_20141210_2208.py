# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursera', '0004_auto_20141210_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='group_id',
            new_name='group',
        ),
    ]
