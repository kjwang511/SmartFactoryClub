# Generated by Django 2.1.4 on 2019-01-21 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='section',
            new_name='category',
        ),
    ]
