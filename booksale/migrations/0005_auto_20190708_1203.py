# Generated by Django 2.2.3 on 2019-07-08 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksale', '0004_auto_20190708_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='count',
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('Mystery', 'Mystery'), ('Biographies', 'Biographies'), ('Sci-fi', 'Sci-fi and Fantasy'), ('Horror', 'Horror'), ('Kids', 'Kids'), ('Comics', 'Comics'), ('generic', 'generic')], default='generic', max_length=100),
        ),
    ]
