# Generated by Django 2.2.10 on 2020-09-01 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0007_auto_20200901_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='note_category',
            field=models.CharField(choices=[('Uncategorized', 'Uncategorized'), ('Work', 'Work'), ('Family', 'Family Affair'), ('Study', 'Study'), ('Personal', 'Personal')], default='', max_length=200),
        ),
    ]
