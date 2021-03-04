from django.db import models
from django.conf import settings

class Habit(models.Model):
    title = models.CharField(max_length=500)
    target_unit = models.CharField(max_length=140)
    target_value = models.PositiveIntegerField()
    period_length = models.PositiveIntegerField()
    rhythm = models.PositiveIntegerField()


    pass

class HabitPeriod(models.Model):
    habit = models.ForeignKey(Habit,
                              related_name='periods',
                              on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()

    pass

class HabitLog(models.Model):
    pass
