# Generated by Django 3.2.5 on 2021-07-22 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_alter_user_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_email',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]