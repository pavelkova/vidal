from django.contrib import admin
from .models import Card, NoteCard, LinkCard, CardAttachment, Reference, Comment, Link, LinkAttachment, Activity

admin.site.register(Card)
admin.site.register(NoteCard)
admin.site.register(LinkCard)
admin.site.register(Link)
admin.site.register(Reference)
admin.site.register(Comment)
admin.site.register(Activity)
