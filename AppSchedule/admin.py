from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(TPriorityDimension)
class TPriorityDimensionAdmin(admin.ModelAdmin):
    # 列表页属性
    # 显示字段
    list_display = ['id', 'name', 'weight_ratio', 'is_delete', 'updated_datetime']
    # 过滤条件
    list_filter = ['name']
    # 搜索字段
    search_fields = ['name']
    # 分页
    list_per_page = 10


@admin.register(TPrioritySelect)
class TPrioritySelectAdmin(admin.ModelAdmin):
    # 列表页属性
    # 显示字段
    list_display = ['id', 'dimension_id', 'name', 'outline', 'weight_ratio', 'is_delete', 'updated_datetime']
    # 过滤条件
    list_filter = ['name']
    # 搜索字段
    search_fields = ['name']
    # 分页
    list_per_page = 50
