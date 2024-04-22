# user_interface.py

class UserInterface:
    def __init__(self, weather_forecast):
        self.weather_forecast = weather_forecast

    def get_weather_info(self, city, detailed=False):
        if detailed:
            return self.weather_forecast.get_weather_forecast(city)
        else:
            data = self.weather_forecast.get_weather_forecast(city)
            if "Weather data not available" not in data:
                return data
            else:
                return f"Weather data not available for {city}"
