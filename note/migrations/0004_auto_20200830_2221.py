# Generated by Django 2.2.10 on 2020-08-30 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20200830_2022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='note_category',
        ),
    ]