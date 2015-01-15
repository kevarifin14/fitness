from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from fitstart.models import Exercise, Workout, ExerciseType, Challenge, Event

#where I write my forms

class WorkoutForm(ModelForm):
	class Meta:
		model = Workout
		fields = [
			'name', 'exercise_one', 'reps_one', 'timed_one', 'exercise_two', 'reps_two', 'timed_two', 'exercise_three', 'reps_three', 'timed_three',
			'exercise_four', 'reps_four', 'timed_four', 'exercise_five', 'reps_five', 'timed_five', 'exercise_six', 'reps_six', 'timed_six',
		]

class ExerciseForm(ModelForm):
	class Meta:
		model = Exercise
		fields = ['exercise_type', 'exercise_name']

class EventForm(ModelForm):
	start = forms.DateField(widget=SelectDateWidget())
	end = forms.DateField(widget=SelectDateWidget())
	class Meta: 
		model = Event
		fields = ['workout', 'start', 'end']