# Generated by Django 3.1.2 on 2020-12-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20201207_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='vk_link',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Идентификатор пользователя во вконтакте'),
        ),
    ]