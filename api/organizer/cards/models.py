from django.db import models
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver

from base import models as base_models

class Page(models.Model):
    title = models.CharField(max_length=140, default=None)
    cards = models.ManyToManyField(Card,
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
    # description = models.CharField(max_length=1000, default=None)
    pass

class PositionedCard(models.Model):
    position = models.PositiveIntegerField()
    card = models.ForeignKey('Card',
                             default=None,
                             on_delete=models.CASCADE)
    page = models.ForeignKey(Page,
                             default=None,
                             on_delete=models.CASCADE)
    section = models.ForeignKey(Section, null=True, on_delete=models.CASCADE)
    is_minimized = models.BooleanField(default=False)
    pass

class CardItem(models.Model):
    position = models.PositiveIntegerField()
    card = models.ForeignKey('Card',
                             default=None,
                             on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    mime_type = models.CharField(max_length=140) # ?
    content = models.TextField()
    # media = single or ordered gallery of embedded or uploaded photo/video

    # note
    # link - title (char), url (url)
    # saved web page - title, link,
    # task
    # gallery - title
    ## item: position, image url/field, video url/filefield, description
    # code block
    pass

class CardTemplate(models.Model):
    # user - optional, for custom templates
    properties = models.JSONField()
    # context
    pass
