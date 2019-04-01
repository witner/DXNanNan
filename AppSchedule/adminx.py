from .models import *
import xadmin


class TPriorityDimensionAdminX(object):
    pass


class TPrioritySelectAdminX(object):
    pass


class TPriorityAdminX(object):
    pass


class TPlanningAdminX(object):
    pass


class TMilestoneAdminX(object):
    pass


class TTodoAdminX(object):
    pass


class TScheduleAdminX(object):
    pass


class TScheduleFollowAdminX(object):
    pass


xadmin.site.register(TPriorityDimension, TPriorityDimensionAdminX)
xadmin.site.register(TPrioritySelect, TPrioritySelectAdminX)
xadmin.site.register(TPriority, TPriorityAdminX)
xadmin.site.register(TPlanning, TPlanningAdminX)
xadmin.site.register(TMilestone, TMilestoneAdminX)
xadmin.site.register(TTodo, TTodoAdminX)
xadmin.site.register(TSchedule, TScheduleAdminX)
xadmin.site.register(TScheduleFollow, TScheduleFollowAdminX)
