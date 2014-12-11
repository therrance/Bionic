# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursera', '0002_auto_20141210_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_id',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
