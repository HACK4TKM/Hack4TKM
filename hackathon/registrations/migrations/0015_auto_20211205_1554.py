# Generated by Django 3.1.13 on 2021-12-05 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0014_auto_20211205_1547'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='top',
            options={'ordering': ['team__team_name'], 'verbose_name': 'Topper', 'verbose_name_plural': 'Toppers'},
        ),
    ]
