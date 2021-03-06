# Generated by Django 3.1.2 on 2020-11-13 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_event_looking_for_a_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='going_to_participate',
            field=models.ManyToManyField(blank=True, related_name='going_to_participate', through='content.Intent', to='content.Profile', verbose_name='Собираются учавствовать'),
        ),
        migrations.AlterField(
            model_name='event',
            name='looking_for_a_company',
            field=models.ManyToManyField(blank=True, related_name='looking_for_a_company_to', to='content.Profile', verbose_name='Ищут компанию'),
        ),
    ]
