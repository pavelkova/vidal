class Item():
    created_at = models.CharField()
    updated_at = models.CharField()
    # references = models.ManyToMany()
    pass

class Note():
    pass

class Link():
    url = models.CharField()
    pass

class Quote():
    source_title = models.CharField()
    source_link = models.CharField()
    pass

class Task():
    due = models.DateTimeField()
    scheduled = models.DateTimeField()

    pass

class Habit():
'''
GOALIFY ->
goal: {
  subject: target_unit,
  type: ,
  timing: {
    start: start_date,
    end: end_date,
    period:
    rhythm:
    rhythmInit:
  },
  targetdefinitions: {
    targets: [{
-- if type == 'avoid': value == -1
-- if
      value: target_quantity
    }]
  }
}
'''
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    target_quantity = models.Integer() # goalify -> goal.targetdefinitions.
    target_unit = models.CharField() # one of list or custom
    target
    pass

class Media():
    # has template with specific properties per type, like film (director, year)
    # may include link to file? ex. for book
    pass

#####
# DISPLAY & LINK MODELS

class Card():
    # primary item one of the above
    # however, certain item types have restricted subitems
    # ex. habit--primary purpose is to show logs and backlinks
    comments = models.ForeignKey()
    references = models.ForeignKey() # reference from one card to another is a link; reference to a card from a page is inclusion
    activity = models.ForeignKey()
    pass

#####
# CATEGORIES

class Realm():
    # required for task, project, time log? has default?
    pass

class TagCategory():
    # special categories for special cards
    pass

class Tag():
    pass

#####
# PAGES

class Page():
    pass

class Section():
    pass

class Project(Page):
    pass

class Collection(Page):
    pass

class Library(Page):
    pass

#####
# ACTIVITY LOGS
class ActivityLog():
    actions = [('CREATED', 'created'),
               ('UPDATED', 'updated'),
               ('REFERENCED', 'referenced')] # page would have: card added
    pass

class TimeLog():
    realm = models.ForeignKey(Realm)
    start = models.DateTimeField()
    end = models.DateTimeField()
    duration = models.DateTimeField()

    pass

class TaskLog():
    task = models.ForeignKey(Task) # this task has time logs associated with it and cannot be deleted. you can archive it to hide it outside previous log contexts
    default_statuses = [('TODO', 'todo'),
                        ('INPROGRESS', 'in progress'),
                        ('PARTIAL', 'partially completed')
                        ('POSTPONED', 'postponed'),
                        ('CANCELLED', 'cancelled'),
                        ('DONE', 'done')]
    # when timer starts: inprogress
    # when marked done: (if habit & habit type is task/avoid) mark habit done
    # when timer stops for tasks associated with duration goals: add duration to habit
    status = models.CharField(choices=TASK_STATUSES)

# PAGES, CARDS, ACTIVITIES
# TOP-LEVEL ITEMS
# SUB ITEMS
# REFERENCES

# CONTEXT --
class Context():
    # type = [all tasks, all pages, specific page, specific task, all cards, specific card type, specific page type]
    default_tags = models.ManyToManyField(Tag)
    excluded_tags = models.ManyToManyField(Tag)
    required_tag_categories = models.ManyToManyField(Tag)
    excluded_tag_categories = models.ManyToManyField(Tag)

class Task():
    context = models.ForeignKey(Context)

# tag context, activity context
# Specifc task -> context
# User -> task settings -> context
# note: in view, respond to certain keys by providing autocomplete menu for references; when processing text, collect that

class Reference():
    origin = models.ManyToManyField(Card)
    is_inline = models.BooleanField(default=False) # true if reference came from within a note
    description = models.CharField() # an optional short description of why the reference is being made--unless is inline, in which case the description will be truncated text surrounding the reference
    location = models.ManyToManyField(Card)
    created_at = models.DateTimeField(auto_add_now)

class ActivityLog():
