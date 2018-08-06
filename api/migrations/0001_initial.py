# Generated by Django 2.0.7 on 2018-08-06 18:54

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('amount', models.FloatField(default=0)),
                ('timestamp', models.BigIntegerField()),
                ('contributionVehicle', models.TextField()),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('groupType', models.CharField(max_length=256)),
                ('goalType', models.CharField(max_length=256)),
                ('goalNote', models.CharField(max_length=256)),
                ('timestamp', models.BigIntegerField(default=0)),
                ('allowNotifications', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupSaving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('month', models.CharField(max_length=256)),
                ('groupType', models.CharField(max_length=256)),
                ('goalType', models.CharField(max_length=256)),
                ('amount', models.FloatField(default=0)),
                ('phoneNumber', models.CharField(max_length=256)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InputStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('backspaceCount', models.IntegerField(default=0)),
                ('totalKeyPressCount', models.IntegerField(default=0)),
                ('timeStartTyping', models.BigIntegerField(default=0)),
                ('timeStopTyping', models.BigIntegerField(default=0)),
                ('timeSpentInField', models.BigIntegerField(default=0)),
                ('finalInputValue', models.CharField(max_length=256)),
                ('finalInputLength', models.IntegerField(default=0)),
                ('intelliWordChanges', models.TextField(blank=True, null=True)),
                ('intelliWordIndex', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PageStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('timestamp', models.BigIntegerField()),
                ('timeSpent', models.BigIntegerField()),
                ('previousPage', models.CharField(max_length=256)),
                ('pageName', models.CharField(max_length=256)),
                ('pageOrder', models.IntegerField()),
                ('isInputPresent', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('phoneNumber', models.CharField(max_length=256, unique=True)),
                ('deviceBuild', models.CharField(max_length=256)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='pagestat',
            name='registration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Registration'),
        ),
        migrations.AddField(
            model_name='inputstat',
            name='pageStat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.PageStat'),
        ),
        migrations.AddField(
            model_name='goal',
            name='registration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Registration'),
        ),
        migrations.AddField(
            model_name='contribution',
            name='goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Goal'),
        ),
    ]
