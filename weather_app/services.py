from weather_api.settings import API_KEY
from datetime import datetime, timedelta
import requests


class WeatherService:
    @staticmethod
    def format_response(user, item):
        utc_time = datetime.strptime(item['dt_txt'], "%Y-%m-%d %H:%M:%S")

        utc_brazil = utc_time - timedelta(hours=3)

        return {

            "location": f"{user.city}, {user.state}",
            "temp": item['main']['temp'],
            "feels_like": item['main']['feels_like'],
            "description": item['weather'][0]['description'],
            "humidity": item['main']['humidity'],
            "date_time": utc_brazil.strftime('%d/%m/%Y %H:%M')

        }

    @staticmethod
    def format_today_weather_response(user, item):
        utc_time = datetime.fromtimestamp(item['dt'])

        utc_brazil = utc_time - timedelta(hours=3)
        return {
            "location": f"{user.city},{user.state} ",
            "temp": item['main']['temp'],
            "feels_like": item['main']['feels_like'],
            "description": item['weather'][0]['description'],
            "humidity": item['main']['humidity'],
            "date_time": utc_brazil.strftime('%d/%m/%Y %H:%M')
        }

    @staticmethod
    def get_weather_by_location(location_name):

        geo_url = "http://api.openweathermap.org/geo/1.0/direct"
        params = {
            'q': location_name,
            'limit': 1,
            'appid': API_KEY,
        }

        geo_response = requests.get(geo_url, params=params).json()

        if not geo_response:
            return None

        lat = geo_response[0]['lat']
        lon = geo_response[0]['lon']

        weather_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=pt_br"
        weather_response = requests.get(weather_url).json()

        if not weather_response:
            return None


        return weather_response

    @staticmethod
    def get_today_weather(location_name):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location_name}&appid={API_KEY}&units=metric&lang=pt_br"
        return requests.get(url).json()