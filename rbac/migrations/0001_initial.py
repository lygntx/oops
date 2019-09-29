# Generated by Django 2.2.4 on 2019-09-28 16:08

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='菜单名')),
                ('icon', models.CharField(blank=True, max_length=50, null=True, verbose_name='图标')),
                ('is_show', models.BooleanField(default=True, verbose_name='显示标记')),
                ('component', models.CharField(blank=True, max_length=200, null=True, verbose_name='组件')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rbac.Menu', verbose_name='父菜单')),
            ],
            options={
                'verbose_name': '菜单',
                'verbose_name_plural': '菜单',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='权限')),
                ('path', models.CharField(max_length=128, unique=True, verbose_name='权限URL')),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rbac.Menu', verbose_name='所属菜单')),
            ],
            options={
                'verbose_name': '权限',
                'verbose_name_plural': '权限',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='角色')),
                ('desc', models.CharField(blank=True, max_length=50, null=True, verbose_name='描述')),
                ('permissions', models.ManyToManyField(blank=True, to='rbac.Permission', verbose_name='权限')),
            ],
            options={
                'verbose_name': '角色',
                'verbose_name_plural': '角色',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('real_name', models.CharField(default='', max_length=50, verbose_name='姓名')),
                ('image', models.ImageField(default='image/default.png', upload_to='avatar/%Y/%m/%d', verbose_name='头像')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('roles', models.ManyToManyField(to='rbac.Role', verbose_name='角色')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
