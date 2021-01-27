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


class ActionItem(models.Model):
    pass


class Activity(models.Model):

    class Meta:
        verbose_name_plural = 'activities'

    verb = models.CharField(max_length=140, default='created')
    action = models.ForeignKey('ActionItem',
                               null=True,
                               on_delete=models.CASCADE)
    target = models.ForeignKey(Card,
                               default=None,
                               related_name='activities',
                               on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    # utc_timestamp = models.DateTimeField(auto_now_add=True)
    # tz = models.CharField()
    # date = models.DateField()
    pass


class CardType(models.Model):
    card = models.OneToOneField(Card,
                                default=None,
                                primary_key=True,
                                on_delete=models.CASCADE)

    def save_activity(self, verb='created'):
        activity = Activity(verb=verb, target=self.card)
        activity.save()
        print(activity)
        return activity

    class Meta:
        abstract = True


class NoteCard(CardType):
    content = models.TextField()

    def __str__(self):
        return self.content


class LinkCard(CardType):
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


class CardAttachment(models.Model):
    action = models.OneToOneField(ActionItem,
                                  default=None,
                                  primary_key=True,
                                  on_delete=models.CASCADE)
    card = models.ForeignKey(Card,
                             default=None,
                             related_name='%(class)s',
                             on_delete=models.CASCADE)

    def save_activity(self, verb='created'):
        activity = Activity(verb=verb, action=self.action, target=self.card)
        activity.save()
        print(activity)
        return activity

    class Meta:
        abstract=True


class Comment(CardAttachment):
    content = models.CharField(max_length=1200)
    pass


class LinkAttachment(CardAttachment):
    link = models.ForeignKey('Link',
                             default=None,
                             on_delete=models.CASCADE)
    pass

class NoteRevision(CardAttachment):
    note = models.ForeignKey('NoteCard',
                             default=None,
                             on_delete=models.CASCADE)
    content = models.TextField()
    pass

class NoteInlineItem(models.Model):
    note = models.ForeignKey('NoteCard',
                             default=None,
                             on_delete=models.CASCADE)

    class Meta:
        abstract=True

class InlineLink(NoteInlineItem):
    link = models.ForeignKey('Link',
                             default=None,
                             on_delete=models.CASCADE)
    pass

class InlineReference(NoteInlineItem):
    referemce = models.ForeignKey('Reference',
                                  default=None,
                                  on_delete=models.CASCADE)
    pass

# comment added to card
# reference made to card
# revision made to note
# status change to task
# time log added (to task/project/realm)
# movie watched (template card / custom verb)

# template card
# template card log
