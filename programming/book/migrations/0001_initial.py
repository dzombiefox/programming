# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=25, verbose_name='Title')),
                ('author', models.CharField(max_length=25, verbose_name='Author')),
                ('publish_at', models.DateField()),
                ('number_of_page', models.IntegerField()),
                ('type_of_book', models.CharField(default='nov', max_length=25, choices=[('nov', 'one of novel'), ('doc', 'documentation'), ('oth', 'other')])),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
