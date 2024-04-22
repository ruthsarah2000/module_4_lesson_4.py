# weather_forecast.py

class WeatherForecast:
    def __init__(self, data_fetcher, data_parser):
        self.data_fetcher = data_fetcher
        self.data_parser = data_parser

    def get_weather_forecast(self, city):
        data = self.data_fetcher.fetch_weather_data(city)
        return self.data_parser.parse_weather_data(data)
