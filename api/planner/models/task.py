from django.db import models
from django.conf import settings

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

class TaskCard(models.Model):
    task = models.OneToOneField(Task,
                                on_delete=models.CASCADE,
                                parent_link=True,
                                primary_key=True,
                                related_name='main_of')
    description = models.TextField()
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    is_repeatable = models.BooleanField(default=False)

    pass

class StatusChange(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    from_status = models.CharField(max_length=140,
                                   choices=default_statuses,
                                   default='TODO')
    to_status = models.CharField(max_length=140,
                                 choices=default_statuses,
                                 default='DONE')
    pass

class Comment(models.Model):
    card = models.ForeignKey(TaskCard, on_delete=models.CASCADE)
    content = models.TextField()

class Link(models.Model):
    card = models.ForeignKey(TaskCard, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    url = models.URLField()
    description = models.TextField()

    pass

class Attachment(models.Model):
    pass
