from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=140)
    pass


default_statuses = [('TODO', 'todo'),
                    ('INPROGRESS', 'in progress'),
                    ('PARTIAL', 'partially completed'),
                    ('POSTPONED', 'postponed'),
                    ('CANCELLED', 'cancelled'),
                    ('DONE', 'done')]

class Task(models.Model):
    title = models.CharField(max_length=500)
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, related_name='subtask', on_delete=models.CASCADE)
    status = models.CharField(max_length=140, choices=default_statuses, default='TODO')
    is_repeatable = models.BooleanField(default=False)
    pass


calendar_entry_types = [('DUE', 'due'),
                        ('SCHEDULED', 'scheduled'),
                        ('EVENT', 'event')]

class CalendarEntry(models.Model):

    class Meta:
        verbose_name_plural = 'calendar entries'

    entry_type = models.DateTimeField(choices=calendar_entry_types)
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
