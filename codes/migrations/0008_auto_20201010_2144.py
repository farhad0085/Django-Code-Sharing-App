# Generated by Django 3.0.10 on 2020-10-10 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0007_auto_20201010_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='snippet_body',
            field=models.TextField(verbose_name='Code Snippet'),
        ),
        migrations.AlterField(
            model_name='code',
            name='snippet_title',
            field=models.CharField(default='', max_length=1000, verbose_name='Title/Filename'),
        ),
    ]
