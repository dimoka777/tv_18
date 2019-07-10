# Generated by Django 2.2.2 on 2019-07-10 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_tv', '0003_auto_20190709_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tv_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('price', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='tv_choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='site_tv.Choice'),
        ),
    ]
