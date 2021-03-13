import sys
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from django.shortcuts import render
from django.conf import settings
from django.db import connection
from django.http import JsonResponse, HttpResponseServerError
from webapp import models
import datetime
from random import randint

#from main import logAll

def index(request):
    data = models.Log.objects.all().values()
    res = list(data)
    #return JsonResponse(res, safe=False)
    for el in res:
        el['time'] = el['time'].timestamp()
    return render(request, 'index.html', context={
        'last_reads': res
    })


def add(request):
    res = models.Log(datetime.datetime.now(), randint(5,25), randint(10, 90), randint(10, 90)).save()
    return JsonResponse(res, safe=False)

def read(request):
    if settings.DEBUG:
        return JsonResponse({'hum': 1})

    try:
        res = logAll()
        return JsonResponse(res)
    except Exception as e:
        return HttpResponseServerError(e)

def logAll():
    record = Log(time=datetime.now)
    try:
        values = com.read(com.Sensors.ALL)
        for k, v in values:
            if isinstance(v, com.ProtoException):
                values[k] = None
                record.msg = '' if not record.msg else record.msg + \
                    str(v) + '; '
        record.hum = values['hum']
        record.soil = values['soil']
        record.temp = values['temp']
    except Exception as e:
        record.msg = str(e)
    finally:
        record.save()
        return record
