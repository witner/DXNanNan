# Generated by Django 2.1.7 on 2019-03-23 09:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppEvent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TMilestone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('outline', models.CharField(max_length=128)),
                ('complete_datetime', models.DateTimeField()),
                ('complete_reward', models.CharField(default='无', max_length=128)),
                ('state', models.IntegerField(choices=[(1, '未开始'), (2, '进行中'), (3, '已完成'), (4, '已放弃')], default=0)),
                ('progress_rate', models.IntegerField(default=0)),
                ('sequence', models.IntegerField(default=1)),
                ('is_delete', models.BooleanField(default=False)),
                ('created_datetime', models.DateTimeField()),
                ('updated_datetime', models.DateTimeField()),
                ('created_by_id', models.ForeignKey(on_delete=None, related_name='t_milestone_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 't_milestone',
            },
        ),
        migrations.CreateModel(
            name='TPlanning',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('outline', models.CharField(max_length=128)),
                ('priority_fraction', models.IntegerField(default=100)),
                ('priority_detail', models.CharField(default='空', max_length=256)),
                ('complete_datetime', models.DateTimeField()),
                ('complete_reward', models.CharField(default='无', max_length=128)),
                ('state', models.IntegerField(choices=[(1, '未开始'), (2, '进行中'), (3, '已完成'), (4, '已放弃')], default=0)),
                ('progress_rate', models.IntegerField(default=0)),
                ('is_delete', models.BooleanField(default=False)),
                ('created_datetime', models.DateTimeField()),
                ('updated_datetime', models.DateTimeField()),
                ('created_by_id', models.ForeignKey(on_delete=None, related_name='t_planning_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by_id', models.ForeignKey(on_delete=None, related_name='t_planning_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 't_planning',
            },
        ),
        migrations.CreateModel(
            name='TPriority',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.IntegerField(choices=[(1, '重要程度'), (2, '紧急程度'), (3, '难易程度'), (4, '所属情况')])),
                ('outline', models.CharField(max_length=32)),
                ('type_proportion', models.IntegerField()),
                ('outline_proportion', models.IntegerField()),
                ('is_delete', models.BooleanField(default=False)),
                ('created_datetime', models.DateTimeField()),
                ('updated_datetime', models.DateTimeField()),
                ('created_by_id', models.ForeignKey(on_delete=None, related_name='t_priority_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by_id', models.ForeignKey(on_delete=None, related_name='t_priority_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 't_priority',
            },
        ),
        migrations.CreateModel(
            name='TSchedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('outline', models.CharField(max_length=128)),
                ('detail', models.TextField(blank=True, null=True)),
                ('priority_fraction', models.IntegerField()),
                ('priority_detail', models.CharField(blank=True, default='空', max_length=256, null=True)),
                ('state', models.IntegerField(choices=[(1, '未开始'), (2, '进行中'), (3, '已完成'), (4, '已放弃')], default=0)),
                ('progress_rate', models.IntegerField(default=0)),
                ('number', models.IntegerField(choices=[(0, '循环'), (1, '单次')], default=1)),
                ('start_datetime_plan', models.DateTimeField(blank=True, null=True)),
                ('end_datetime_plan', models.DateTimeField(blank=True, null=True)),
                ('start_datetime_adjust', models.DateTimeField(blank=True, null=True)),
                ('end_datetime_adjust', models.DateTimeField(blank=True, null=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('created_datetime', models.DateTimeField()),
                ('updated_datetime', models.DateTimeField()),
                ('created_by_id', models.ForeignKey(on_delete=None, related_name='t_schedule_created_by', to=settings.AUTH_USER_MODEL)),
                ('event_tag_id', models.ForeignKey(blank=True, null=True, on_delete=None, to='AppEvent.TEventTag')),
                ('event_type_id', models.ForeignKey(on_delete=None, to='AppEvent.TEventType')),
                ('execute_by_id', models.ForeignKey(on_delete=None, related_name='t_schedule_execute_by', to=settings.AUTH_USER_MODEL)),
                ('milestone_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=None, related_name='t_schedule_milestone_id', to='AppSchedule.TMilestone')),
                ('planning_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=None, related_name='t_schedule_planning_id', to='AppSchedule.TPlanning')),
            ],
            options={
                'db_table': 't_schedule',
            },
        ),
        migrations.CreateModel(
            name='TScheduleFollow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('notes', models.TextField()),
                ('is_delete', models.BooleanField(default=False)),
                ('created_datetime', models.DateTimeField()),
                ('updated_datetime', models.DateTimeField()),
                ('created_by_id', models.ForeignKey(on_delete=None, related_name='t_schedule_follow_created_by', to=settings.AUTH_USER_MODEL)),
                ('schedule_id', models.ForeignKey(on_delete=None, related_name='t_schedule_follow_schedule_id', to='AppSchedule.TSchedule')),
                ('updated_by_id', models.ForeignKey(on_delete=None, related_name='t_schedule_follow_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 't_schedule_follow',
            },
        ),
        migrations.CreateModel(
            name='TTodo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('outline', models.CharField(max_length=128)),
                ('is_delete', models.BooleanField(default=False)),
                ('created_datetime', models.DateTimeField()),
                ('updated_datetime', models.DateTimeField()),
                ('created_by_id', models.ForeignKey(on_delete=None, related_name='t_todo_created_by', to=settings.AUTH_USER_MODEL)),
                ('milestone_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=None, related_name='t_todo_milestone_id', to='AppSchedule.TMilestone')),
                ('planning_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=None, related_name='t_todo_planning_id', to='AppSchedule.TPlanning')),
                ('updated_by_id', models.ForeignKey(on_delete=None, related_name='t_todo_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 't_todo',
            },
        ),
        migrations.AddField(
            model_name='tschedule',
            name='todo_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, related_name='t_schedule_todo_id', to='AppSchedule.TTodo'),
        ),
        migrations.AddField(
            model_name='tschedule',
            name='updated_by_id',
            field=models.ForeignKey(on_delete=None, related_name='t_schedule_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tmilestone',
            name='planning_id',
            field=models.ForeignKey(on_delete=None, related_name='t_milestone_planning_id', to='AppSchedule.TPlanning'),
        ),
        migrations.AddField(
            model_name='tmilestone',
            name='updated_by_id',
            field=models.ForeignKey(on_delete=None, related_name='t_milestone_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
