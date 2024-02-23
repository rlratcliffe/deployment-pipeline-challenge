from django.db import models

class Order(models.Model):
    trace_id = models.CharField(max_length=60)
    abbreviated_name = models.CharField(max_length=60)
    food_ordered = models.CharField(max_length=60)
    started_status = models.BooleanField(default=False)
    processing_status = models.BooleanField(default=False)