from django.db import models
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils.translation import gettext_lazy as _

from base import models as base_models

class Page(models.Model):
    title = models.CharField(max_length=140, default=None)
    cards = models.ManyToManyField('Card',
                                   through='PositionedCard')
    pass

class Section(models.Model):
    title = models.CharField(max_length=140, default=None)
    page = models.ForeignKey(Page,
                             default=None,
                             on_delete=models.CASCADE)
    pass

class Card(models.Model):
    title = models.CharField(max_length=140, default=None)
    parent = models.ForeignKey(Page,
                               default=None,
                               on_delete=models.CASCADE)

    # description = models.CharField(max_length=1000, default=None)
    pass


class Position(models.Model):
    position = models.PositiveIntegerField()
    card = models.ForeignKey(Card,
                             default=None,
                             on_delete=models.CASCADE)
    class Meta:
        abstract=True


class PositionedCard(Position):
    page = models.ForeignKey(Page,
                             default=None,
                             on_delete=models.CASCADE)
    section = models.ForeignKey(Section, null=True, on_delete=models.CASCADE)
    is_minimized = models.BooleanField(default=False)
    pass

class CardItem(Position):
    # parent = models.ForeignKey('self',
    #                            null=True,
    #                            default=None,
    #                            related_name='children',
    #                            on_delete=models.CASCADE)
    # depth = models.PositiveIntegerField(default=0)
    # media = single or ordered gallery of embedded or uploaded photo/video

    # note
    # link - title (char), url (url)
    # saved web page - title, link,
    # task
    # gallery - title
    ## item: position, image url/field, video url/filefield, description
    # code block
    pass

class Note(CardItem):
    class Meta:
        proxy = True

class InlineObject(models.Model):
    inline = models.BooleanField(default=False)

    class Meta:
        abstract=True


class Link(models.Model):
    description = models.CharField(max_length=140)
    url = models.URLField()

class MediaItem(models.Model):
    mime_type = models.CharField(max_length=500)
    url = models.URLField()
    attachment = models.FileField(null=True)
    pass

class MediaGalleryItem(models.Model):
    item = models.ForeignKey(MediaItem, default=None, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    position = models.PositiveIntegerField()
    pass

class MediaGallery(models.Model):
    items = models.ManyToManyField('MediaItem',
                                   through='MediaGalleryItem')
    pass


class Reference(models.Model):
    to_card = models.ForeignKey(Card, null=True, on_delete=models.CASCADE)
    to_page = models.ForeignKey(Page, null=True, on_delete=models.CASCADE)
    from_card = models.ForeignKey(Card, related_name='referrer', on_delete=models.CASCADE)

class Task(models.Model):
    class StatusChoices(models.TextChoices):
        TODO = 'TODO', _('Todo')
        DONE = 'DONE', _('Done')
        INPROGRESS = 'INPROGRESS', _('In progress')
        POSTPONED = 'POSTPONED', _('Postponed')
        CANCELLED = 'CANCELLED', _('Cancelled')

    status = CharField(choices=StatusChoices.choices,
                       default=StatusChoices.TODO)
    pass

class ThingOfFiniteTime(models.Model):
    timezone = models.CharField(max_length=140)
    start = models.DateTimeField(default=None)
    end = models.DateTimeField(null=True)

    class Meta:
        abstract=True

class Habit(models.Model):
    pass

class CalendarEntry(models.Model):
    pass

class Recurrence(models.Model):
    pass

################################

class Link(models.Model):
    pass

class Reference(models.Model):
    pass

class CalendarEvent(models.Model):
    pass

class Media(models.Model):
    pass

class Log(models.Model):
    pass

class Comment(models.Model):
    content = models.TextField()
    pass

class Activity(models.Model):
    pass

class SpecialProperties(models.Model):
    # schema json
    # schema validation
    pass

class CardTemplate(models.Model):
    pass

class LogTemplate(models.Model):
    pass

class Timeline(models.Model):
    pass

class Context(models.Model):
    pass

# default templates

class TimeLog(models.Model):
    start = models.DateTimeField(default=None)
    end = models.DateTimeField(null=True)
    pass

class Habit(models.Model):
    pass

class HabitLog(models.Model):
    pass

class Media(models.Model):
    # book, article, movie, video, music
    pass

class MediaLog(models.Model):
    # verb: (to read, read), (to watch, watched), (unlistened, listened)
    pass

class Task(models.Model):
    pass

class TaskLog(models.Model):
    pass

class Exercise(models.Model):
    title = models.CharField(max_length=500)
    # equipment options
    # log options
    # media gallery
    description = models.TextField()
    pass

class ExerciseLog(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    pass

class ExerciseGroup(models.Model):
    title = models.CharField(max_length=500)
    exercises = models.ManyToManyField(Exercise)
    pass

class Workout(models.Model):

    pass

class WorkoutLog(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(ExerciseLog)
    pass
