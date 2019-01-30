# Generated by Django 2.1.4 on 2019-01-28 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(help_text='不允许与其他条目重复。', max_length=25, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='不允许与其他条目重复。', max_length=25, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='name',
            field=models.CharField(help_text='不允许与其他条目重复。', max_length=25, verbose_name='名称'),
        ),
    ]