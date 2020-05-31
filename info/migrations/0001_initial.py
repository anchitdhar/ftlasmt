# Generated by Django 3.0.6 on 2020-05-30 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.CharField(editable=False, max_length=30, primary_key=True, serialize=False, unique=True)),
                ('real_name', models.CharField(max_length=20)),
                ('tz', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('finish_time', models.DateTimeField()),
                ('related_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.User')),
            ],
        ),
    ]
