from django.conf.urls import url
from observations.views import add_weather_reading, add_observation

urlpatterns = [
    url('^add/observations/observation', name='add_observation', view=add_observation),
    url('^add/observations/weather', name='add_weather', view=add_weather_reading)
]