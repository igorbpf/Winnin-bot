# Generated by Django 2.0.4 on 2018-04-12 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Created at'),
        ),
    ]