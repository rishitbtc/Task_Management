# Generated by Django 3.2.5 on 2021-12-03 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_rename_members_projectteam_teammate'),
        ('task', '0003_auto_20211201_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
    ]