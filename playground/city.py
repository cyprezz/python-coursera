import pprint
import requests
from datetime import datetime

class RapidWeatherForecast:
    
    def __init__(self):
        self._city_cache = {}

    def get(self, city):
        if city in self._city_cache:
            return self._city_cache[city]

        url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"
        
        querystring = {"cnt":"10","units":"metric" ,"q":city}

        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "e7d4adf259mshf7f52c7714d5d6dp114ee8jsnae68561f9984"
            }
        print('sending HTTP request')
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        forecast = []
        for day in response['list']:
            forecast.append({
                "date" : datetime.utcfromtimestamp(day['dt']).isoformat(),
                "high_temp" : day['temp']['max']
            })
        self._city_cache[city] = forecast
        return forecast

class CityInfo:

    def __init__(self, city, weather_forecast=None):
        self.city = city
        self._weather_forecast = weather_forecast or RapidWeatherForecast()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city)
        

def _main():
    weather_forecast = RapidWeatherForecast()
    for i in range(5):
        city_info = CityInfo("Odessa,ua", weather_forecast=weather_forecast)
        info = city_info.weather_forecast()
        pprint.pprint(info)

if __name__ == "__main__":
    _main()
    