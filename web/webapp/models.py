from django.db import models

class Log(models.Model):
    time = models.DateTimeField(primary_key = True)
    soil = models.FloatField()
    temp = models.FloatField()
    hum = models.FloatField()
    msg = models.TextField()