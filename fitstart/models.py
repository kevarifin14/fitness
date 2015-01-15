from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class ExerciseType(models.Model):
	category = models.CharField(max_length=20)
	exercise_class = models.CharField(max_length=10, default=None, blank=True, null=True)

	def __str__(self):
		return self.category

	def __repr__(self):
		return self.category


class Exercise(models.Model):
	exercise_name = models.CharField(max_length=50)
	exercise_type = models.ForeignKey(ExerciseType)
	reps = models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		return self.exercise_name

	def __repr__(self):
		return self.exercise_name


class Workout(models.Model):
	name = models.CharField(max_length=50, default=None, null=True)
	exercise_one = models.ForeignKey(Exercise, related_name='one', default=None, null=True)
	reps_one = models.PositiveSmallIntegerField(default=None)
	timed_one = models.NullBooleanField(null=True, default=False)
	
	exercise_two = models.ForeignKey(Exercise, related_name='two', default=None, null=True)
	reps_two = models.PositiveSmallIntegerField(default=None)
	timed_two = models.NullBooleanField(null=True, default=False)
	
	exercise_three = models.ForeignKey(Exercise, related_name='three', default=None, null=True,blank=True)
	reps_three = models.PositiveSmallIntegerField(default=None, null=True, blank=True)
	timed_three = models.NullBooleanField(null=True, default=False)
	
	exercise_four = models.ForeignKey(Exercise, related_name='four', default=None, null=True)
	reps_four = models.PositiveSmallIntegerField(default=None)
	timed_four = models.NullBooleanField(null=True, default=False)
	
	exercise_five = models.ForeignKey(Exercise, related_name='five', default=None, null=True)
	reps_five = models.PositiveSmallIntegerField(default=None)
	timed_five = models.NullBooleanField(null=True, default=False)

	exercise_six = models.ForeignKey(Exercise, related_name='six', default=None, null=True,blank=True)
	reps_six = models.PositiveSmallIntegerField(default=None, null=True, blank=True)
	timed_six = models.NullBooleanField(null=True, default=False)

	def __str__(self):
		return self.name

	def __repr__(sefl):
		return self.name


class Challenge(models.Model):
	name = models.CharField(max_length=50)
	goal = models.CharField(max_length=300, default=None)
	workout = models.ForeignKey(Workout, default=None)

	def __str__(self):
		return self.name

	def __repr__(sefl):
		return self.name

class Event(models.Model):
	workout = models.ForeignKey(Workout)
	start = models.DateField()
	end = models.DateField(null=True, blank=True)

	def __str__(self):
		return self.workout.name

	def __repr__(self):
		return self.workout.name
