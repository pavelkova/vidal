from django.db import models
from django.conf import settings


class CardTemplate(models.Model):
    special_property_fields = {
        'order': 'Integer',
        'field_type': 'String', # limit to primitives
        'form_type': 'String', # e.g. select, textarea
        'options': 'Dict/Array', # e.g. select, radio options, null is unlimited
    }

    name = models.CharField(max_length=500)
    # context
    # maybe this should be an abstract model?
    # or maybe the jsonfield should only be for input argument...create actual
    special_properties = models.JSONField(null=True)
    pass

class LogTemplate(models.Model):
    pass

class UserCardTemplate(models.Model):
    item_fields = {
        'order': 'Integer',
        'item_type': 'String', # limit to titles of CardItem classes
        'is_required': 'Boolean',
        'children': { ... }
    }

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.JSONField(null=True)
    template = models.ForeignKey(CardTemplate, on_delete=models.CASCADE)
    pass
