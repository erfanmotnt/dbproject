# Generated by Django 3.1.6 on 2021-02-03 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mhbank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='tname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mhbank.tag'),
        ),
    ]