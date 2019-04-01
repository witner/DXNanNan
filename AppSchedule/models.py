from django.db import models
from django.contrib.auth.models import User
from AppEvent.models import TEventType, TEventTag

# Create your models here.


class TPriorityDimension(models.Model):
    '''
    优先级维度
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)

    # 权重占比 10 代表 10%， 默认10%
    weight_ratio = models.IntegerField(default=10)

    is_delete = models.BooleanField(default=False)
    updated_datetime = models.DateTimeField()

    class Meta:
        db_table = 't_priority_dimension'
        ordering = ['-weight_ratio']

    def __str__(self):
        return self.name


class TPrioritySelect(models.Model):
    '''
    优先级选择
    '''
    id = models.AutoField(primary_key=True)
    dimension_id = models.ForeignKey(TPriorityDimension, on_delete=models.CASCADE, related_name='select')
    name = models.CharField(max_length=16)
    outline = models.CharField(max_length=256, default=u'无', blank=True)

    # 权重占比 10 代表 10%， 默认10%
    weight_ratio = models.IntegerField(default=10)

    is_delete = models.BooleanField(default=False)
    updated_datetime = models.DateTimeField()

    class Meta:
        db_table = 't_priority_select'

    def __str__(self):
        return self.name


class TPriority(models.Model):
    id = models.AutoField(primary_key=True)
    TYPE = (
        (1, u'重要程度'),
        (2, u'紧急程度'),
        (3, u'难易程度'),
        (4, u'所属情况'),
    )
    type = models.IntegerField(choices=TYPE)
    outline = models.CharField(max_length=32)
    # 优先级类型占比 10 代表 10%
    type_proportion = models.IntegerField()
    # 优先级描述占比 10 代表 10%
    outline_proportion = models.IntegerField()

    is_delete = models.BooleanField(default=False)
    created_by_id = models.ForeignKey(User, related_name='t_priority_created_by', on_delete=None)
    created_datetime = models.DateTimeField()
    updated_by_id = models.ForeignKey(User, related_name='t_priority_updated_by', on_delete=None)
    updated_datetime = models.DateTimeField()

    class Meta:
        db_table = 't_priority'

    def __str__(self):
        return self.outline

    def get_fraction(self):
        return self.type_proportion * self.outline_proportion / 100

# 通用


class TPlanning(models.Model):
    id = models.AutoField(primary_key=True)
    outline = models.CharField(max_length=128)
    # 优先级分数，总分数100
    priority_fraction = models.IntegerField(default=100)
    # 优先级详情
    priority_detail = models.CharField(max_length=256, default=u'空')
    # 目标完成日期时间
    complete_datetime = models.DateTimeField()
    # 完成奖励
    complete_reward = models.CharField(max_length=128, default=u'无')
    STATE_TYPE = (
        (1, u"未开始"),
        (2, u"进行中"),
        (3, u"已完成"),
        (4, u'已放弃'),
    )
    state = models.IntegerField(choices=STATE_TYPE, default=0)
    # 进度0~100%
    progress_rate = models.IntegerField(default=0)

    is_delete = models.BooleanField(default=False)
    created_by_id = models.ForeignKey(User, related_name='t_planning_created_by', on_delete=None)
    created_datetime = models.DateTimeField()
    updated_by_id = models.ForeignKey(User, related_name='t_planning_updated_by', on_delete=None)
    updated_datetime = models.DateTimeField()

    class Meta:
        db_table = 't_planning'

    def __str__(self):
        return self.outline

    @classmethod
    def create(cls, _outline, _priority_fraction, _priority_detail, _complete_datetime, _complete_reward, _state, _progress_rate,
               _is_delete, _created_by_id, _created_datetime, _updated_by_id, _updated_datetime):
        obj = cls(outline=_outline,
                  priority_fraction=_priority_fraction,
                  priority_detail=_priority_detail,
                  complete_datetime=_complete_datetime,
                  complete_reward=_complete_reward,
                  state=_state,
                  progress_rate=_progress_rate,
                  is_delete=_is_delete,
                  created_by_id=_created_by_id,
                  created_datetime=_created_datetime,
                  updated_by_id=_updated_by_id,
                  updated_datetime=_updated_datetime)
        return obj


class TMilestone(models.Model):
    id = models.AutoField(primary_key=True)
    outline = models.CharField(max_length=128)
    # 完成日期时间
    complete_datetime = models.DateTimeField()
    # 完成奖励
    complete_reward = models.CharField(max_length=128, default=u'无')
    STATE_TYPE = (
        (1, u"未开始"),
        (2, u"进行中"),
        (3, u"已完成"),
        (4, u'已放弃'),
    )
    state = models.IntegerField(choices=STATE_TYPE, default=0)
    # 进度0~100%
    progress_rate = models.IntegerField(default=0)

    planning_id = models.ForeignKey(TPlanning, related_name='t_milestone_planning_id', on_delete=None)
    sequence = models.IntegerField(default=1)

    is_delete = models.BooleanField(default=False)
    created_by_id = models.ForeignKey(User, related_name='t_milestone_created_by', on_delete=None)
    created_datetime = models.DateTimeField()
    updated_by_id = models.ForeignKey(User, related_name='t_milestone_updated_by', on_delete=None)
    updated_datetime = models.DateTimeField()

    class Meta:
        db_table = 't_milestone'

    def __str__(self):
        return self.outline

    @classmethod
    def create(cls, _outline, _complete_datetime, _complete_reward, _state, _progress_rate, _planning_id, _sequence,
               _is_delete, _created_by_id, _created_datetime, _updated_by_id, _updated_datetime):
        obj = cls(outline=_outline,
                  complete_datetime=_complete_datetime,
                  complete_reward=_complete_reward,
                  state=_state,
                  progress_rate=_progress_rate,
                  planning_id=_planning_id,
                  sequence = _sequence,
                  is_delete=_is_delete,
                  created_by_id=_created_by_id,
                  created_datetime=_created_datetime,
                  updated_by_id=_updated_by_id,
                  updated_datetime=_updated_datetime)
        return obj


class TTodo(models.Model):
    # 待办事项
    id = models.AutoField(primary_key=True)
    # outline 清单概述
    outline = models.CharField(max_length=128)

    planning_id = models.ForeignKey(TPlanning, related_name='t_todo_planning_id', on_delete=None, default=None,
                                    blank=True, null=True)
    milestone_id = models.ForeignKey(TMilestone, related_name='t_todo_milestone_id', on_delete=None, default=None,
                                     blank=True, null=True)

    is_delete = models.BooleanField(default=False)
    created_by_id = models.ForeignKey(User, related_name='t_todo_created_by', on_delete=None)
    created_datetime = models.DateTimeField()
    updated_by_id = models.ForeignKey(User, related_name='t_todo_updated_by', on_delete=None)
    updated_datetime = models.DateTimeField()

    class Meta:
        db_table = 't_todo'

    def __str__(self):
        return self.outline

    @classmethod
    def create(cls, _outline, _planning_id, _milestone_id,
               _is_delete, _created_by_id, _created_datetime, _updated_by_id, _updated_datetime):
        obj = cls(outline=_outline,
                  planning_id=_planning_id,
                  milestone_id=_milestone_id,
                  is_delete=_is_delete,
                  created_by_id=_created_by_id,
                  created_datetime=_created_datetime,
                  updated_by_id=_updated_by_id,
                  updated_datetime=_updated_datetime)
        return obj


class TSchedule(models.Model):
    # 清单表
    id = models.AutoField(primary_key=True)
    outline = models.CharField(max_length=128)
    # 细节信息
    detail = models.TextField(blank=True, null=True)

    event_type_id = models.ForeignKey(TEventType, on_delete=None)
    event_tag_id = models.ForeignKey(TEventTag, on_delete=None, blank=True, null=True)
    # 优先级分数，总分数100
    priority_fraction = models.IntegerField()
    # 优先级详情
    priority_detail = models.CharField(max_length=256, default=u'空', blank=True, null=True)

    STATE_TYPE = (
        (1, u"未开始"),
        (2, u"进行中"),
        (3, u"已完成"),
        (4, u'已放弃'),
    )
    state = models.IntegerField(choices=STATE_TYPE, default=0)
    # 进度0~100%
    progress_rate = models.IntegerField(default=0)
    NUMBER_TYPE = (
        (0, u'循环'),
        (1, u'单次'),
    )
    number = models.IntegerField(choices=NUMBER_TYPE, default=1)

    # start_time_plan = models.TimeField(blank=True, null=True)
    # end_time_plan = models.TimeField(blank=True, null=True)
    # start_time_adjust = models.TimeField(blank=True, null=True)
    # end_time_adjust = models.TimeField(blank=True, null=True)

    start_datetime_plan = models.DateTimeField(blank=True, null=True)
    end_datetime_plan = models.DateTimeField(blank=True, null=True)
    start_datetime_adjust = models.DateTimeField(blank=True, null=True)
    end_datetime_adjust = models.DateTimeField(blank=True, null=True)

    execute_by_id = models.ForeignKey(User, related_name='t_schedule_execute_by', on_delete=None)
    #place = models.CharField(max_length=128)
    todo_id = models.ForeignKey(TTodo, related_name='t_schedule_todo_id', on_delete=None, blank=True, null=True)
    planning_id = models.ForeignKey(TPlanning, related_name='t_schedule_planning_id', on_delete=None, blank=True,
                                    null=True, default=None)
    milestone_id = models.ForeignKey(TMilestone, related_name='t_schedule_milestone_id', on_delete=None, blank=True,
                                     null=True, default=None)

    is_delete = models.BooleanField(default=False)
    created_by_id = models.ForeignKey(User, related_name='t_schedule_created_by', on_delete=None)
    created_datetime = models.DateTimeField()
    updated_by_id = models.ForeignKey(User, related_name='t_schedule_updated_by', on_delete=None)
    updated_datetime = models.DateTimeField()

    class Meta:
        db_table = 't_schedule'

    @classmethod
    def create(cls, _outline, _detail, _event_type_id, _event_tag_id, _priority_fraction, _priority_detail,
               _state, _progress_rate, _number,
               # _start_time_plan, _end_time_plan, _start_time_adjust, _end_time_adjust,
               _start_datetime_plan, _end_datetime_plan, _start_datetime_adjust, _end_datetime_adjust,
               _execute_by_id, _todo_id, _planning_id, _milestone_id,
               _is_delete, _created_by_id, _created_datetime, _updated_by_id, _updated_datetime):
        obj = cls(outline=_outline,
                  detail=_detail,
                  event_type_id=_event_type_id,
                  event_tag_id=_event_tag_id,
                  priority_fraction=_priority_fraction,
                  priority_detail=_priority_detail,
                  state=_state,
                  progress_rate=_progress_rate,
                  number=_number,
                  # start_time_plan=_start_time_plan,
                  # end_time_plan=_end_time_plan,
                  # start_time_adjust=_start_time_adjust,
                  # end_time_adjust=_end_time_adjust,
                  start_datetime_plan=_start_datetime_plan,
                  end_datetime_plan=_end_datetime_plan,
                  start_datetime_adjust=_start_datetime_adjust,
                  end_datetime_adjust=_end_datetime_adjust,
                  execute_by_id=_execute_by_id,
                  todo_id=_todo_id,
                  planning_id=_planning_id,
                  milestone_id=_milestone_id,
                  is_delete=_is_delete,
                  created_by_id=_created_by_id,
                  created_datetime=_created_datetime,
                  updated_by_id=_updated_by_id,
                  updated_datetime=_updated_datetime)
        return obj


class TScheduleFollow(models.Model):
    # 清单跟进
    id = models.AutoField(primary_key=True)
    # 跟进记录
    notes = models.TextField()

    schedule_id = models.ForeignKey(TSchedule, related_name='t_schedule_follow_schedule_id', on_delete=None)

    is_delete = models.BooleanField(default=False)
    created_by_id = models.ForeignKey(User, related_name='t_schedule_follow_created_by', on_delete=None)
    created_datetime = models.DateTimeField()
    updated_by_id = models.ForeignKey(User, related_name='t_schedule_follow_updated_by', on_delete=None)
    updated_datetime = models.DateTimeField()

    class Meta:
        db_table = 't_schedule_follow'

    @classmethod
    def create(cls, _notes, _schedule_id,
               _is_delete, _created_by_id, _created_datetime, _updated_by_id, _updated_datetime):
        obj = cls(
            notes=_notes,
            schedule_id=_schedule_id,
            is_delete=_is_delete,
            created_by_id=_created_by_id,
            created_datetime=_created_datetime,
            updated_by_id=_updated_by_id,
            updated_datetime=_updated_datetime)
        return obj
