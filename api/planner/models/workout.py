from django.db import models
from django.conf import settings

class Exercise(models.Model):
    title = models.CharField(max_length=500)
    equipment_options = models.ManyToManyField('ExerciseEquipment')
    # set_options = duration, duration + weight, reps only, assisted reps, reps + weights
    # equipment options
    # log options
    # media gallery
    description = models.TextField()
    pass

class ExerciseEquipment(models.Model):
    title = models.CharField(max_length=140)
    pass

class SetType(models.Model):
    title = models.CharField(max_length=140)
    pass

class SetTypeLog(models.Model):
    # duration = models.
    # reps = models.PositiveIntegerField()
    # weight = models.
    is_assisted = models.BooleanField(default=False)
    position = models.PositiveIntegerField()
    pass

class ExerciseLog(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    equipment = models.ForeignKey(ExerciseEquipment, on_delete=models.CASCADE)
    pass

class ExerciseGroup(models.Model):
    title = models.CharField(max_length=500)
    exercises = models.ManyToManyField(Exercise)
    pass

class Workout(models.Model):
    exercises = models.ManyToManyField(Exercise)
    pass

class WorkoutLog(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(ExerciseLog)
    pass
