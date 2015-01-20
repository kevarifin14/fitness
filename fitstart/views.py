from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import render

from fitstart.models import Exercise, Workout, ExerciseType, Challenge, Event, Quotation
from fitstart.forms import WorkoutForm, ExerciseForm, EventForm

import datetime, calendar, random
from datetime import date, timedelta, time

#  your views here.

class HomeView(generic.ListView):
	template_name = 'fitstart/home.html'
	context_object_name = 'exercise_list'

	def get_queryset(self):
		return Exercise.objects.order_by('exercise_type')

class ExerciseView(generic.ListView):
	template_name = 'fitstart/exercise.html'
	context_object_name = 'exercise_list'

	def get_queryset(self):
		pass

def add_exercise(request):
	form = ExerciseForm(request.POST or None)

	if form.is_valid():
		saved = form.save(commit=False)
		saved.save()
		return HttpResponseRedirect('')

	return render(request, "fitstart/add.html", {'form': form})

class RepositoryView(generic.ListView):
	template_name = 'fitstart/repository.html'
	context_object_name = 'exercise_list'

	def get_queryset(self):
		return Exercise.objects.order_by('exercise_type')

class WorkoutView(generic.ListView):
	template_name = 'fitstart/workout.html'
	context_object_name = 'workout_list'

	def get_queryset(self):
		return Workout.objects.order_by('name')

def create_workout(request):
	form = WorkoutForm(request.POST or None)
	
	if form.is_valid():
		saved = form.save(commit=False)
		saved.save()
		return HttpResponseRedirect('')

	return render(request, "fitstart/create.html", {'form': form})

class CollectionView(generic.ListView):
	template_name = 'fitstart/collection.html'
	context_object_name = 'workout_list'

	def get_queryset(self):
		return Workout.objects.order_by('name')


class ChallengeView(generic.ListView):
	template_name = 'fitstart/challenge.html'
	context_object_name = 'challenge_list'

	def get_queryset(self):
		return Challenge.objects.order_by('name')

def create_calendar(request):
	template = 'fitstart/calendar.html'
	events = Event.objects.order_by('start')
	cal = calendar.Calendar()
	week_iter = cal.iterweekdays()
	today = datetime.datetime.now()
	week = [today]
	now = datetime.datetime.now()
	number = random.randint(1,1)
	quotation = Quotation.objects.get(pk=number)
	
	for day in week_iter:
		mod = timedelta(days=1)
		today = today + mod
		week.append(today)

	context = {
		'event_list': events,
		'now': now,
		'week': week,
		'quotation': quotation,
	}
	return render(request, template, context)

def create_event(request, workout_id):
	form = EventForm(data=request.POST or None, initial={'workout': Workout.objects.get(pk=workout_id), 'start': datetime.date.today(), 'end': datetime.date.today()})

	if form.is_valid():
		saved = form.save(commit=False)
		saved.save()
		return HttpResponseRedirect('')

	return render(request, "fitstart/event.html", {'form': form})