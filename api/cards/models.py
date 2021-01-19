
from django.db import models

# Create your models here.

# references
# history
# task, event, habit
# note, link, media


class Item():
    # id
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    # created_at
    # updated_at
    # references
    # history
    title = models.CharField(null=False)
    is_archived = models.BooleanField()
    is_deleted = models.BooleanField()

    # description
    pass


class Card():
    primary_item = models.GenericForeignKey()
    tags = models.ManyToManyField()
    # top-level item: note, link, media, task, habit
    # subitems: checklist (subtasks), comments, attachment, cover, link, quote, referenced by, history
    pass

class SubItem():
    # parent: { id, type, order, is_primary_item }
    # if type == card, comment, reference, no is_primary_item
    pass

class Note():
    pass

class Link():
    url = models.URLField()

class Reference():
    referenced_card = models.ForeignKey()

    # properties: read-write inclusion, read-only inclusion, link only

class Attachment():
    file = models.FileField()



# top-level: note, task, link, media
# sub-level only: comment, reference
# user settings: task statuses
## ACTIVITIES
class Task():
    # TODO move these defs to top of file or make them user settings
    default_statuses = ('TODO', 'INPROGRESS', 'POSTPONED', 'CANCELLED', 'DONE')
    default_statuses_enum = ENUM(*default_statuses, name="status")
    all_day = Column(Boolean, default=False)
    # project_id
    timezone = models.CharField()
    time_estimate = Column(Integer)
    status = Column(default_statuses_enum)
    scheduled_date = models.DateTimeField()
    due_date = models.DateTimeField()
    # history activity_types: { status_change: { new_status: time }}
    # repeating task: history - completed, postponed, failed
    # card inclusion

class Habit():
    # frequency
    periods = ('DAILY', 'WEEKLY', 'MONTHLY')
    periods_enum = ENUM(*periods, name="period")
    # PERIOD PARAMETERS
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday']
    weekly_day_count = [1..6]
    monthly_day_count = [1..31]
    monthly_week_count = [1..5]
    # PERIOD + PARAM combinations:
    # DAILY + any combination of WEEKDAYS (default: all)
    # --- default: meet the target every day
    # --- with selection (e.g. M, T, W): meet the target every M, T, W
    # WEEKLY + any one of WEEKLY_DAY_COUNT (default: 1)
    # --- default: meet the target once per week
    # --- with selection (e.g. 4): meet the target 4 times per week
    # MONTHLY + any one of MONTHLY_DAY_COUNT (default: 1) as quantity
    # -- default: meet the target once per month
    # -- with selection (e.g. 10): meet the target 10 times per month
    # MONTHLY + any combination of MONTHLY_DAY_COUNT (default: 1) as date
    # -- default: meet the target on the first of every month
    # -- with selection (e.g. 1, 15) meet the target on the 1st and 15th of every month
    # MONTHLY + array of any combinations of (MONTHLY_WEEK_COUNT + WEEKDAY) (default: 1 + Monday)
    # -- default: meet the target on the first monday of every month
    # -- with selection (e.g. [1,3 + Monday; 5 + Friday]): meet the target on the first and third monday and the fifth friday of every month
    # target_quantity -- default: 1
    # target_unit -- (special types--time) -- default: times -- (combo target "1 time" == is_boolean)
    # history: change target
    target_quantity = models.PositiveIntegerField()
    target_unit = models.CharField() # goalify -> goal.subject

    target_type = ['boolean', 'duration']
    # for Habits with duration target type - target unit = hours or minutes
    auto_add_tags = models.ManyToManyField()
    auto_add_projects = models.ManyToManyField()
    auto_add_realms = models.ManyToManyField()

    pass

class HabitLog():
    # activity: { add_amount, at }
    #
    # date:
    # quantity_recorded
    # percent_completed
    # quantity_type = add_to_total or update_total -- add_to_total by default, but load last used per habit
    pass

class TimeLog():
    parent_id { TASK, PROJECT, REALM }
    start = models.DateTimeField()
    end = models.DateTimeField()
    duration = models.DurationField()
    description = models.TextField()
    # tags


class History():
    # date
    # activity_type
    # activity_details
    # on card: added subitem, was referenced by, edited text block or note
    default_activity_types = ['created', 'updated', 'referemced_by', 'archived', 'deleted', 'time_log']


class TagCategory():
    pass

class Tag():
    tag_category = models.ForeignKey(TagCategory,
                                     od_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

class Project():
    # inherit Page model
    default_tags = models.ManyToManyField(Tag)
    exclude_tags = models.ManyToManyField(Tag)
    exclude_tag_categories = models.ManyToManyField(TagCategory)
    require_tag_categories = models.ManyToManyField(TagCategory)

class PageSection():
    page = models.ForeignKey(Page,
                             on_delete=models.CASCADE)
    name = models.CharField()
    manual_card_order = models.ManyToManyField()
    order_method = models.CharField()
    # ascending date, descending date, manual, ascending name, descending name

custom activities
activity logs

Habit -> belong to realm, fed by completed tasks, time logs (by tag, task, or project)

ActivitySequence:
(timelog - task/realm/project id, sequence id)
(sequencelog - task logs, start/finish)
(one click to stop current task and start next in sequence)

user settings: Default pomodoro break activity

# SPECIAL CARD TYPES
# media: direct parent is library page, can be included elsewhere
