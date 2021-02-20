import graphene
from graphene_django import DjangoObjectType

from .models import Card, Activity, NoteCard, LinkCard, Link, Reference, CardAttachment, Comment, LinkAttachment, NoteRevision, NoteInlineItem, InlineLink, InlineReference, CardType, ActionItem

class CardType(DjangoObjectType):
    class Meta:
        model = Card
        fields = ('user', 'title', 'references')

class ActivityType(DjangoObjectType):
    class Meta:
        model = Activity
        fields = ('verb', 'action', 'target', 'timestamp')
