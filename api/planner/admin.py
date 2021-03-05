from django.contrib import admin
# from .models.habit import Habit, HabitPeriod, HabitLog
from .models.task import Project, Task, Subtask, TaskCard
from .models.time import CalendarEntry
from .models.habit import Habit, HabitPeriod, HabitLog
from .models.workout import Workout, WorkoutLog, Exercise, ExerciseEquipment, ExerciseGroup, ExerciseLog

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Subtask)
admin.site.register(TaskCard)
admin.site.register(CalendarEntry)
admin.site.register(Habit)
admin.site.register(HabitPeriod)
admin.site.register(HabitLog)
admin.site.register(Workout)
admin.site.register(WorkoutLog)
admin.site.register(Exercise)
admin.site.register(ExerciseEquipment)
admin.site.register(ExerciseGroup)
admin.site.register(ExerciseLog)
