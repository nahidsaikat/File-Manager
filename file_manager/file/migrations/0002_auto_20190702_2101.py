# Generated by Django 2.2.3 on 2019-07-02 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='path',
        ),
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(default='asdf', upload_to='documents/'),
            preserve_default=False,
        ),
    ]
