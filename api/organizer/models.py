from django.db import models
from django.conf import settings

class Card(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey('CardItem', on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=140, default=None)
    references = models.ManyToManyField('self',
                                        through='Reference',
                                        through_fields=('to_card', 'from_card'))
    comments = models.ForeignKey('Comment', null=True, on_delete=models.CASCADE)
    activities = models.ForeignKey('Activity', null=True, on_delete=models.CASCADE)
    pass


class Reference(models.Model):
    to_card = models.ForeignKey(Card, on_delete=models.CASCADE)
    from_card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='referee')
    pass

class Comment(models.Model):
    content = models.CharField(max_length=1200)
    pass


class CardItem(models.Model):
    pass

class Note(models.Model):
    card = models.OneToOneField(CardItem, on_delete=models.CASCADE, primary_key=True)
    content = models.TextField()
    pass


class Link(models.Model):
    card = models.OneToOneField(CardItem, on_delete=models.CASCADE, primary_key=True)
    url = models.URLField()
    pass

class Activity(models.Model):
    # VERB_CHOICES = [('CREATED', 'created'),
    #                 ('UPDATED', 'updated',
    #                  'REFERENCED', 'referenced',
    #                  'INCLUDED')]
    verb = models.CharField(max_length=140, default=None)
    action = models.ForeignKey('ActionItem', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # target = models.ForeignKey(Card, on_delete=models.CASCADE)
    # target = ActionTarget (Card, Page, Realm) -- maybe through inverse
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
