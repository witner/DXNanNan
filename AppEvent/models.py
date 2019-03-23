from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TEventType(models.Model):
    id = models.IntegerField(primary_key=True)
    outline = models.CharField(max_length=32)
    LEVEL_TYPE = (
        (1, "一级事件"),
        (2, "二级事件"),
        (3, "三级事件"),
    )
    level = models.IntegerField(choices=LEVEL_TYPE)
    parent_event_id = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)
    created_by_id = models.ForeignKey(User, related_name='t_event_type_created_by', on_delete=None)
    created_datetime = models.DateTimeField()
    updated_by_id = models.ForeignKey(User, related_name='t_event_type_updated_by', on_delete=None)
    updated_datetime = models.DateTimeField()

    class Meta:
        db_table = 't_event_type'

    def __str__(self):
        return self.outline


class TEventTag(models.Model):
    id = models.AutoField(primary_key=True)
    outline = models.CharField(max_length=32)
    is_delete = models.BooleanField(default=False)
    created_by_id = models.ForeignKey(User, related_name='t_event_tag_created_by', on_delete=None)
    created_datetime = models.DateTimeField()
    updated_by_id = models.ForeignKey(User, related_name='t_event_tag_updated_by', on_delete=None)
    updated_datetime = models.DateTimeField()

    class Meta:
        db_table = 't_event_tag'

    def __str__(self):
        return self.outline
