# Generated by Django 3.2.5 on 2021-07-25 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0004_auto_20210725_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='clicks',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='views',
        ),
        migrations.RemoveField(
            model_name='advertiser',
            name='clicks',
        ),
        migrations.RemoveField(
            model_name='advertiser',
            name='views',
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('ip', models.GenericIPAddressField()),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='advertiser_management.ad')),
            ],
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('ip', models.GenericIPAddressField()),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clicks', to='advertiser_management.ad')),
            ],
        ),
    ]
