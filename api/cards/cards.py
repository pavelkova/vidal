from django.db import models


class Card(models.Model):
    title = models.CharField()
    item = models.ForeignKey(CardItem, on_delete=models.CASCADE)
    # history:
    pass

class CardItem():
    # note, web link, quote,
    # task, recurring task, event, habit
    # library template: film, book, article, etc
    pass

class CardSubItem():
    # comment, web link, reference link, quote
    # subtask (on task card only?), checklist
    pass

# link can be top-level, reference cannot
# text block types: note, comment, description
# note can be top-level, comment and description cannot (description can be field on top-level)
# link or reference can be added within body of top-level note, or separately with a description
# note has revision history, comment and description do not
# TOP-LEVEL ITEMS
class Link(models.Model):
    title = models.CharField()
    url = models.URLField()
    pass

class Note(models.Model):
    content = models.TextField()
    # activity logs: revisions
    pass

class Quote(models.Model):
    author = models.CharField()
    source = models.CharField()
    source_location = models.CharField() # link or attachment/media reference
    pass

class Attachment(models.Model):
    file = models.FileField()
    # add as: media type -- Book, Article, Movie, Video,

class Comment(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pass

class Reference(models.Model):
    to_card = models.ForeignKey()
    from_card = models.ForeignKey()
    pass


# Article, Book, Web Page,

class CardInclusion():
    page = models.ForeignKey(Page)
    section = models.ForeignKey(Section)
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField()
    pass

class TagContext():
    # values wil be inherited from parent + global
    # can belong to page, realm, recurring tasks/habits
    default_tags = model.ManyToManyField()
    exclude_tags = models.ManyToManyField()
    exclude_tag_categories = models.ManyToManyField()
    require_tag_categories = models.ManyToManyField()
    pass

class Tag():
    category = models.ForeignKey(TagCategory)
    pass

class TagCategory():
    title = models.CharField()
    exclusive_to_context = models.ForeignKey(TagContext)
    pass
