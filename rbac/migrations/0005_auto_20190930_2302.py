# Generated by Django 2.2.4 on 2019-09-30 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_auto_20190930_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='显示标记'),
        ),
    ]