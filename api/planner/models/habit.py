from django.db import models
from django.conf import settings

class Habit(models.Model):
    title = models.CharField(max_length=500)
    target_unit = models.CharField(max_length=140)
    target_value = models.PositiveIntegerField()
    period_length = models.SmallIntegerField() # in days or months
    rhythm = models.PositiveIntegerField() # how many periods in a repeating pattern
    pass

class HabitPeriod(models.Model):
    habit = models.ForeignKey(Habit,
                              related_name='periods',
                              on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()

    pass

class HabitLog(models.Model):
    period = models.ForeignKey(HabitPeriod,
                               related_name='logs',
                               on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField()

    pass
