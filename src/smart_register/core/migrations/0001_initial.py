# Generated by Django 3.2.12 on 2022-03-04 09:01

import django.contrib.postgres.fields.citext
import django.db.models.deletion
import strategy_field.fields
from django.contrib.postgres.operations import CITextExtension
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        CITextExtension(),
    ]
