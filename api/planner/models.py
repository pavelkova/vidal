from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=140, default=None)
    parent = models.ForeignKey('self',
                               null=True,
                               default=None,
                               related_name='subprojects',
                               models.on_delete=DELETE)
    pass


default_statuses = [('TODO', 'todo'),
                    ('INPROGRESS', 'in progress'),
                    ('POSTPONED', 'postponed'),
                    ('CANCELLED', 'cancelled'),
                    ('DONE', 'done')]

class TaskCard(models.Model):
    main = models.OneToOneField(Task)
    description = models.TextField()
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    is_repeatable = models.BooleanField(default=False)
    pass

class Task(models.Model):
    title = models.CharField(max_length=500, default=None)
    status = models.CharField(max_length=140,
                              choices=default_statuses,
                              default='TODO')
    due = models.ForeignKey('CalendarEntry', on_delete=models.CASCADE)
    scheduled = models.ForeignKey('CalendarEntry', on_delete=models.CASCADE)
    subtasks = models.ManyToManyField('self',
                                      through='Subtasks',
                                      through_fields=('parent', 'subtask'))
    pass

class Subtask(model.Model):
    parent = models.ForeignKey(Task, on_delete=models.CASCADE)
    subtask = models.ForeignKey(Task, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()
    pass

calendar_entry_types = [('DUE', 'due'),
                        ('SCHEDULED', 'scheduled'),
                        ('EVENT', 'event')]

class CalendarEntry(models.Model):

    class Meta:
        verbose_name_plural = 'calendar entries'

    entry_type = models.CharField(choices=calendar_entry_types)
    date = models.DateTimeField(default=None)
    is_all_day = models.BooleanField(default=True)

    # @property is_overdue
    pass


class Recurrence(models.Model):
    start_date = models.DateTimeField(default=None)
    end_date = models.DateTimeField(null=True)
    period = models.CharField(max_length=140)
    frequency = models.CharField(max_length=140)

    class Meta:
        abstract=True

    pass
