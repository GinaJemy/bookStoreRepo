# Generated by Django 2.2.3 on 2019-07-08 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booksale', '0009_auto_20190708_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='category',
            new_name='cat',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='categ',
        ),
    ]
