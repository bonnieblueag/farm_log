from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from core.views import get_add_model_form
from observations.models import WeatherReading, Observation
from observations.forms import WeatherReadingForm, ObservationForm

ADD_OBSERVATION_TEMPLATE = 'observations/add_observation_model.html'


def add_weather_reading(request):
    return get_add_model_form(request, ADD_OBSERVATION_TEMPLATE, WeatherReading, 'Weather Reading', 'datetime', WeatherReadingForm)


def add_observation(request):
    return get_add_model_form(request, ADD_OBSERVATION_TEMPLATE, Observation, 'Observation', 'observation_date', ObservationForm)

