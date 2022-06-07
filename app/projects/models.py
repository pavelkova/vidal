import uuid
from django.db import models
from django.conf import settings


class Project(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500, default=None)
    parent = models.ForeignKey('self',
                               blank=True,
                               null=True,
                               default=None,
                               related_name='subprojects',
                               on_delete=models.CASCADE)
    # color
    # icon

    def __str__(self):
        return self.title


class Section(models.Model):
    project = models.ForeignKey(Project,
                                blank=True,
                                null=True,
                                default=None,
                                on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500,
                             default=None)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


default_statuses = [('TODO', 'todo'),
                    ('INPROGRESS', 'in progress'),
                    ('POSTPONED', 'postponed'),
                    ('CANCELLED', 'cancelled'),
                    ('DONE', 'done')]


class Task(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500,
                             default=None)
    status = models.CharField(max_length=140,
                              choices=default_statuses,
                              default='TODO')
    # due = models.ForeignKey(CalendarEntry,
    #                         blank=True,
    #                         null=True,
    #                         related_name='due_tasks',
    #                         on_delete=models.CASCADE)
    # scheduled = models.ForeignKey(CalendarEntry,
    #                               blank=True,
    #                               null=True,
    #                               related_name='scheduled_tasks',
    #                               on_delete=models.CASCADE)
    is_repeatable = models.BooleanField(default=False)
    card = models.ForeignKey('TaskCard',
                             default=None,
                             related_name='task_tree',
                             on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    subtasks = models.ManyToManyField('self',
                                      through='Subtask',
                                      through_fields=('parent','child'))
    def __str__(self):
        return self.title


class Subtask(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey(Task,
                               related_name='supertask',
                               on_delete=models.CASCADE)
    child = models.ForeignKey(Task,
                              on_delete=models.CASCADE)
    position = models.PositiveIntegerField()
    pass


class Habit(models.Model):
    pass

class HabitPeriod(models.Model):
    pass

class HabitLog(models.Model):
    pass

class TagCategory(models.Model):
    pass

class Tag(models.Model):
    pass

class TagContext(models.Model):
    pass

class Routine(models.Model):
    pass
