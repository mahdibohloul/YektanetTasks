# Generated by Django 3.2.5 on 2021-07-25 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='advertiser',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='advertiser_management.advertiser'),
            preserve_default=False,
        ),
    ]