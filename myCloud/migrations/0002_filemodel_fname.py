# Generated by Django 2.0.4 on 2018-04-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCloud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='fname',
            field=models.CharField(default='', max_length=100, verbose_name='文件名'),
            preserve_default=False,
        ),
    ]
