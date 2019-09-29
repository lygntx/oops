# Generated by Django 2.2.4 on 2019-09-29 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0002_menu_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='component',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='组件'),
        ),
        migrations.AddField(
            model_name='permission',
            name='icon',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='图标'),
        ),
    ]
