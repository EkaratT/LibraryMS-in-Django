# Generated by Django 4.1.4 on 2022-12-18 10:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('is_referrence_only', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('available', 'Available'), ('loned', 'Loned'), ('lost', 'Lost')], default='available', max_length=50)),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.author')),
            ],
            options={
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=200, null=True, unique=True)),
                ('membership_date', models.DateTimeField(auto_now_add=True)),
                ('membership_status', models.CharField(choices=[('active', 'Active'), ('closed', 'Closed'), ('blacklist', 'Blacklist')], default='active', max_length=20)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IssueBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(auto_now_add=True)),
                ('expired_date', models.DateTimeField(default=datetime.datetime(2023, 1, 2, 10, 45, 38, 246282))),
                ('fine_per_day', models.PositiveIntegerField(default=0)),
                ('over_due', models.BooleanField(blank=True, default=False, null=True)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.book')),
                ('borrower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.member')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.category'),
        ),
    ]
