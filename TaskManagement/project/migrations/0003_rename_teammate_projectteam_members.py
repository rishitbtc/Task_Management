# Generated by Django 3.2.5 on 2021-08-20 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20210820_1541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectteam',
            old_name='teammate',
            new_name='Members',
        ),
    ]
