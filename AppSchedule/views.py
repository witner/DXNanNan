from django.shortcuts import render
from AppSchedule.models import *
from AppEvent.models import *
from AppUser.models import *
from django.contrib.auth.models import User
from django.views.generic import ListView

# Create your views here.

# class TMPListByListView(ListView):
#     if