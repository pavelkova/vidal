from django.db import models
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver

from base import models as base_models
'''
Connection types for data:
- INCLUSION/TRANSCLUSION
  - Cards being included in other pages.
- BELONGS TO
  - For items that are direct descendants of a single card and limited to its scope: e.g. comments,
  - Cards linked to one page as its primary/original parent: e.g. a task card belongs to a project page, an article or book (with metadata template) belongs to a library or collection page.
- REFERENCE

Each of which implies ACTIVITY for both objects.
- (activity)

Plus CONTEXTS:
parent objects opening a variety of special properties, e.g. default tags, workspace exclusive tags,
'''

'''
USER selects 'CREATE CARD'
     enters STRING as card title/text
     --- USER selects 'CARD TYPE' (from menu or by prefixing with keyword) or uses defaul t (default: note, OR user setting, or user last used)
     -> API creates card and associated cardType object
     -> ACTIVITY is created for new card
     --- activity for card and cardtype object are the same:
     --- activity is 'CREATED_AT' when card & initial cardType is created
     --- activity is 'UPDATED_AT' when card is updated (e.g. title field) or when cardtype is updated
     --- activity is 'LAST_ACTIVE_AT' when card is referenced
'''

class Page(models.Model):
    title = models.CharField(max_length=140, default=None)
    # view = column, outline, grid
    # sort_by
    pass

class Section(models.Model):
    title = models.CharField(max_length=140, default=None)
    page = models.ForeignKey(Page,
                               default=None,
                               related_name='sections',
                               on_delete=models.CASCADE)
    # sort_by
    pass


class PositionedCard(models.Model):
    position = models.PositiveIntegerField()
    card = models.ForeignKey('Card',
                             default=None,
                             related_name='included_on',
                             on_delete=models.CASCADE)
    section = models.ForeignKey(Section, null=True, on_delete=models.CASCADE)
    class Meta:
        abstract = True


class Card(base_models.OwnerTimeStamp):
    references = models.ManyToManyField('self',
                                        through='Reference',
                                        through_fields=('to_card', 'from_card'))

    def __str__(self):
        return self.title


class ActionItem(models.Model):
    pass


class Activity(base_models.OwnerStamp):

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
    title = models.CharField(max_length=140, default=None)
    card = models.OneToOneField(Card,
                                default=None,
                                primary_key=True,
                                on_delete=models.CASCADE)

    # def save_activity(self, verb='created'):
    #     activity = Activity(verb=verb, target=self.card)
    #     activity.save()
    #     print(activity)
    #     return activity

    class Meta:
        abstract = True

def create_card_with_type(sender, **kwargs):
    card = Card()
    card.uuid = sender
    card.save()

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
    '''
Link can relate to a card...
AS the primary/top level/one-to-one item
AS a subitem or attachment
AS an <a> tag parsed from the content of a note card
    '''
    description = models.CharField(max_length=140)
    url = models.URLField()
    pass


class Reference(base_models.OwnerStamp):
    to_card = models.ForeignKey(Card,
                                on_delete=models.CASCADE)
    from_card = models.ForeignKey(Card,
                                  related_name='referrer',
                                  on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    pass


class CardAttachment(base_models.OwnerStamp):
    action = models.OneToOneField(ActionItem,
                                  default=None,
                                  primary_key=True,
                                  on_delete=models.CASCADE)
    card = models.ForeignKey(Card,
                             default=None,
                             related_name='%(class)s',
                             on_delete=models.CASCADE)

    # def save_activity(self, verb='created'):
    #     activity = Activity(verb=verb, action=self.action, target=self.card)
    #     activity.save()
    #     print(activity)
    #     return activity

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


class Checklist(CardAttachment):
    pass

class ChecklistItem(models.Model):
    content = models.CharField(max_length=1000)
    checklist = models.ForeignKey(Checklist, default=None, on_delete=models.CASCADE)
    pass
