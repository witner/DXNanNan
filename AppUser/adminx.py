from .models import *
import xadmin


class UserProfileAdminX(object):
    pass


xadmin.site.register(UserProfile, UserProfileAdminX)