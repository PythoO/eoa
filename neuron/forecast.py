"""

"""
import forecastio
import config
from sense.voice import speech
from ui.text import Text

api_key = config.data['forecastio']
lat = config.data['lat']
lng = config.data['lng']

WORDS = {
    'forecast_currently': {
        'groups': [['forecast', 'currently'], ['forecast', 'now'], ['forecasts', 'now'], ['weather', 'now'],
                   ['what', 'weather', 'is', 'it']]},
    'forecast_weekly': {'groups': [['forecast', 'week'], ['forecast', 'weekly']]},
}


def forecast_currently():
    """
    Get the current forecast.
    :return:
    """
    forecast = get_forecast()
    currently = forecast.currently()
    return currently


def forecast_weekly():
    """
    Get the week forecast.
    :return:
    """
    forecast = get_forecast()
    daily = forecast.daily()
    return daily.summary


def get_forecast():
    return forecastio.load_forecast(api_key, lat, lng)
