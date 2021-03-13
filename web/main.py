from webapp.models import *
import os
from django.conf import settings
import django
from datetime import datetime
import time
import schedule
import logger.comunicator as com


# to use django ORM outside django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')
django.setup()


# periodic task

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

# schedule.every(10).minutes.do(log)


while True:
    schedule.run_pending()
    time.sleep(1)
