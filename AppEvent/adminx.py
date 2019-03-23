from .models import *
import xadmin


class TEventTypeAdminX(object):
    pass


class TEventTagAdminX(object):
    pass


xadmin.site.register(TEventType, TEventTypeAdminX)
xadmin.site.register(TEventTag, TEventTagAdminX)
