# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-02 20:08
from __future__ import unicode_literals

from django.db import migrations
import wagtail_i18n.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_i18n', '0010_language_and_locale_ordering'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='language',
            managers=[
                ('objects', wagtail_i18n.models.LanguageManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='locale',
            managers=[
                ('objects', wagtail_i18n.models.LocaleManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='region',
            managers=[
                ('objects', wagtail_i18n.models.RegionManager()),
            ],
        ),
    ]
