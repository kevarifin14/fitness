from django.contrib import admin
from django.forms import ModelForm
from django import forms
from fitstart.models import Exercise, Workout, ExerciseType, Challenge, Event


# Register your models here.

class ExerciseAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['exercise_name','exercise_type']}),
	]
	list_display = ('exercise_name', 'exercise_type')
	list_filter = ['exercise_type']
	search_fields = ['exercise_name']


class WorkoutAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name', 'exercise_one', 'exercise_two', 'exercise_three']})
	]
	list_display = ('name', 'exercise_one', 'exercise_two', 'exercise_three')


CLASSES = (
	('U', 'Upper Body'),
	('L', 'Lower Body'),
	('C', 'Core'),
)


class ExerciseTypeAdminForm(ModelForm):
	exercise_class = forms.MultipleChoiceField(choices=CLASSES)
	fields = ['category', 'exercise_class']
	class Meta:
		model = ExerciseType

class ExerciseTypeAdmin(admin.ModelAdmin):
	form = ExerciseTypeAdminForm

	list_display = ('category',)


class ChallengeAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name', 'goal','workout']})]

class EventAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['title', 'workout']}),
		('Date Information', {'fields': ['start', 'end']}),
	]

admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(ExerciseType, ExerciseTypeAdmin)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Event, EventAdmin)