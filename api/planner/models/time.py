from django.db import models
from django.conf import settings

calendar_entry_types = [('DUE', 'due'),
                        ('SCHEDULED', 'scheduled'),
                        ('EVENT', 'event')]

class CalendarEntry(models.Model):

    class Meta:
        verbose_name_plural = 'calendar entries'

    entry_type = models.CharField(max_length=140,
                                  choices=calendar_entry_types)
    date = models.DateTimeField(default=None)
    is_all_day = models.BooleanField(default=True)

    pass


class Recurrence(models.Model):
    start_date = models.DateTimeField(default=None)
    end_date = models.DateTimeField(null=True)
    period = models.CharField(max_length=140)
    frequency = models.CharField(max_length=140)

    class Meta:
        abstract=True

    pass
