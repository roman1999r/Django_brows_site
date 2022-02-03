import datetime

from django.utils.datetime_safe import time

from .models import *


def endTime(start_time, name):
    proc = Procedure.objects.get(name=name)
    hours_added = datetime.timedelta(hours=proc.time)
    end_time = start_time + hours_added
    return end_time
