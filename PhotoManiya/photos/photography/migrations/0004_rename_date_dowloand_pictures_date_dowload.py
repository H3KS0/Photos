# Generated by Django 3.2.13 on 2024-05-26 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0003_auto_20240527_0021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pictures',
            old_name='date_dowloand',
            new_name='date_dowload',
        ),
    ]
