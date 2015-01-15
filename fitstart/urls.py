from django.conf.urls import patterns, url
from fitstart import views

urlpatterns = patterns('',
	url(r'^$', views.HomeView.as_view(), name='home'),
	url(r'^exercise/$', views.ExerciseView.as_view(), name='exercise'),
	url(r'^exercise/add/$', views.add_exercise, name='add'),
	url(r'^exercise/repository/$', views.RepositoryView.as_view(), name='repository'),
	url(r'^workout/$', views.WorkoutView.as_view(), name='workout'),
	url(r'^workout/create/$', views.create_workout, name='create'),
	url(r'^workout/collection/$', views.CollectionView.as_view(), name='collection'),
	url(r'^workout/event/(?P<workout_id>\d+)/$', views.create_event, name='event'),
	url(r'^challenges/$', views.ChallengeView.as_view(), name='challenge'),
	url(r'^challenges/event/(?P<workout_id>\d+)/$', views.create_event, name='event'),
	url(r'^calendar/$', views.create_calendar, name='calendar'),
)