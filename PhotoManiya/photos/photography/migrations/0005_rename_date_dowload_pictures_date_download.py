# Generated by Django 3.2.13 on 2024-05-26 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0004_rename_date_dowloand_pictures_date_dowload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pictures',
            old_name='date_dowload',
            new_name='date_download',
        ),
    ]