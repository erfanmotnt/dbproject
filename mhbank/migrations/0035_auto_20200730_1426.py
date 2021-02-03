# Generated by Django 3.0.7 on 2020-07-30 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mhbank', '0034_auto_20200721_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='guidance',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='teach_box',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date published'),
        ),
    ]
