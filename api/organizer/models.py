from django.db import models
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver



class Card(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=140, default=None)
    references = models.ManyToManyField('self',
                                        through='Reference',
                                        through_fields=('to_card', 'from_card'))
    def __str__(self):
        return self.title


class NoteCard(models.Model):
    card = models.OneToOneField(Card,
                                default=None,
                                primary_key=True,
                                on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content


class LinkCard(models.Model):
    card = models.OneToOneField(Card,
                                default=None,
                                primary_key=True,
                                on_delete=models.CASCADE)
    link = models.ForeignKey('Link',
                             default=None,
                             on_delete=models.CASCADE)
    pass


class Link(models.Model):
    text = models.CharField(max_length=140)
    url = models.URLField()
    pass


class Reference(models.Model):
    to_card = models.ForeignKey(Card,
                                on_delete=models.CASCADE)
    from_card = models.ForeignKey(Card,
                                  related_name='referrer',
                                  on_delete=models.CASCADE)
    pass


class Comment(models.Model):
    card = models.ForeignKey(Card,
                             default=None,
                             related_name='comments',
                             on_delete=models.CASCADE)
    content = models.CharField(max_length=1200)
    pass


class Activity(models.Model):
    # VERB_CHOICES = [('CREATED', 'created'),
    #                 ('UPDATED', 'updated',
    #                  'REFERENCED', 'referenced',
    #                  'INCLUDED')]
    verb = models.CharField(max_length=140, default='created')
    action = models.ForeignKey('ActionItem',
                               null=True,
                               on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    target = models.ForeignKey(Card,
                               default=None,
                               related_name='activities',
                               on_delete=models.CASCADE)
    pass

class ActionItem(models.Model):
    pass

# comment added to card
# reference made to card
# revision made to note
# status change to task
# time log added (to task/project/realm)
# movie watched (template card / custom verb)

# template card
# template card log
