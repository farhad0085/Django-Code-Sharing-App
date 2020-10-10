# Generated by Django 3.0.10 on 2020-10-10 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0002_auto_20201010_1023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='code',
            old_name='snippet',
            new_name='snippet_body',
        ),
        migrations.AddField(
            model_name='code',
            name='snippet_title',
            field=models.CharField(default='', max_length=1000),
        ),
    ]