# Generated by Django 3.1.6 on 2021-02-03 22:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('username', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('firstname', models.CharField(default='None', max_length=30)),
                ('lastname', models.CharField(default='None', max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=1)),
                ('srate', models.IntegerField(default=0)),
                ('crate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('ename', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('cdate', models.DateTimeField(null=True)),
                ('cusername', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mhbank.account')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('snum', models.IntegerField()),
                ('name', models.CharField(max_length=100, null=True)),
                ('cusername', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sessions', to='mhbank.account')),
                ('ename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mhbank.event')),
                ('tusername', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mhbank.account')),
            ],
            options={
                'unique_together': {('ename', 'snum')},
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('snid', models.IntegerField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(default='None', max_length=30)),
                ('lastname', models.CharField(default='None', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tname', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('cusername', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mhbank.account')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('rsid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('cdate', models.DateTimeField(null=True)),
                ('chdate', models.DateTimeField(null=True)),
                ('chusername', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mhbank.account')),
                ('cusername', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resources', to='mhbank.account')),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=1)),
                ('score', models.IntegerField(default=0)),
                ('text', models.TextField()),
                ('cdate', models.DateTimeField(null=True)),
                ('chdate', models.DateTimeField(null=True)),
                ('ddate', models.DateTimeField(null=True)),
                ('level', models.IntegerField(default=5)),
                ('minaar', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('maxaar', models.IntegerField(default=12, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('vcomment', models.CharField(max_length=1000, null=True)),
                ('chusername', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chproblems', to='mhbank.account')),
                ('cusername', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cproblems', to='mhbank.account')),
                ('dusername', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dproblems', to='mhbank.account')),
                ('rsid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mhbank.resource')),
                ('vusername', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mhbank.account')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('aid', models.IntegerField(primary_key=True, serialize=False)),
                ('anum', models.IntegerField()),
                ('text', models.TextField()),
                ('cdate', models.DateTimeField(null=True)),
                ('chdate', models.DateTimeField(null=True)),
                ('chusername', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mhbank.account')),
                ('cusername', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answers', to='mhbank.account')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mhbank.problem')),
            ],
            options={
                'unique_together': {('pid', 'anum')},
            },
        ),
        migrations.CreateModel(
            name='TeachBox',
            fields=[
                ('tbid', models.IntegerField(primary_key=True, serialize=False)),
                ('explanation', models.TextField(null=True)),
                ('goal', models.TextField(null=True)),
                ('time', models.TimeField(null=True)),
                ('cdate', models.DateTimeField(null=True)),
                ('chdate', models.DateTimeField(null=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mhbank.answer')),
                ('chusername', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mhbank.account')),
                ('cusername', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teachboxes', to='mhbank.account')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mhbank.problem')),
            ],
            options={
                'unique_together': {('pid', 'answer')},
            },
        ),
        migrations.CreateModel(
            name='SubTag',
            fields=[
                ('stid', models.IntegerField(primary_key=True, serialize=False)),
                ('stname', models.CharField(max_length=200)),
                ('cusername', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subtags', to='mhbank.account')),
                ('dusername', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mhbank.account')),
                ('tname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mhbank.tag')),
            ],
            options={
                'unique_together': {('tname', 'stname')},
            },
        ),
        migrations.CreateModel(
            name='STT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('snid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mhbank.student')),
                ('tusername', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mhbank.account')),
            ],
            options={
                'unique_together': {('snid', 'tusername')},
            },
        ),
        migrations.CreateModel(
            name='ST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('snid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mhbank.student')),
                ('tname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mhbank.tag')),
            ],
            options={
                'unique_together': {('snid', 'tname')},
            },
        ),
        migrations.CreateModel(
            name='SP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mhbank.problem')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mhbank.session')),
            ],
            options={
                'unique_together': {('pid', 'sid')},
            },
        ),
        migrations.CreateModel(
            name='PRU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mhbank.problem')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mhbank.account')),
            ],
            options={
                'unique_together': {('pid', 'username')},
            },
        ),
        migrations.CreateModel(
            name='Guidance',
            fields=[
                ('gid', models.IntegerField(primary_key=True, serialize=False)),
                ('gnum', models.IntegerField()),
                ('text', models.TextField()),
                ('cdate', models.DateTimeField(null=True)),
                ('chdate', models.DateTimeField(null=True)),
                ('anum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mhbank.answer')),
                ('chusername', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mhbank.account')),
                ('cusername', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='guidances', to='mhbank.account')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mhbank.problem')),
            ],
            options={
                'unique_together': {('pid', 'gnum')},
            },
        ),
        migrations.CreateModel(
            name='ES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mhbank.event')),
                ('snid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mhbank.student')),
            ],
            options={
                'unique_together': {('ename', 'snid')},
            },
        ),
    ]
