'''
Analyze the provided script and identify distinct functionalities that can be encapsulated into classes. Create classes that 
represent different aspects of the weather forecast application, such as fetching data, parsing data, and user interaction.
Problem Statement:
The existing script for the weather forecast application is written in a procedural style and lacks organization.
'''

# main.py #

from weather_data_fetcher import WeatherDataFetcher
from weather_data_parser import WeatherDataParser
from weather_forecast import WeatherForecast
from user_interface import UserInterface

def main():
    data_fetcher = WeatherDataFetcher()
    data_parser = WeatherDataParser()
    weather_forecast = WeatherForecast(data_fetcher, data_parser)
    user_interface = UserInterface(weather_forecast)

    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = user_interface.get_weather_info(city, detailed=True)
        else:
            forecast = user_interface.get_weather_info(city)
        print(forecast)

if __name__ == "__main__":
    main()
