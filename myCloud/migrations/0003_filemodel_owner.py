# Generated by Django 2.0.4 on 2018-04-29 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCloud', '0002_filemodel_fname'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='owner',
            field=models.CharField(default=2, max_length=20, verbose_name='上传用户'),
            preserve_default=False,
        ),
    ]
