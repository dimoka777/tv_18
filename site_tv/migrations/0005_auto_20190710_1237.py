# Generated by Django 2.2.2 on 2019-07-10 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_tv', '0004_auto_20190710_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='price',
            new_name='tv_price',
        ),
    ]