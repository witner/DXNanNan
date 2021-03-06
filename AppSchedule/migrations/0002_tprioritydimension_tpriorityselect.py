# Generated by Django 2.1.7 on 2019-04-01 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppSchedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TPriorityDimension',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
                ('weight_ratio', models.IntegerField(default=10)),
                ('is_delete', models.BooleanField(default=False)),
                ('updated_datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 't_priority_dimension',
            },
        ),
        migrations.CreateModel(
            name='TPrioritySelect',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
                ('outline', models.CharField(max_length=256)),
                ('weight_ratio', models.IntegerField(default=10)),
                ('is_delete', models.BooleanField(default=False)),
                ('updated_datetime', models.DateTimeField()),
                ('dimension_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='select', to='AppSchedule.TPriorityDimension')),
            ],
            options={
                'db_table': 't_priority_select',
            },
        ),
    ]
