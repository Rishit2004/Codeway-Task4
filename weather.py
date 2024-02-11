import requests

def get_weather(city):
    # API key for OpenWeatherMap
    api_key = 'd1612769c540b74cc9546c0875de6a69'

    # Base URL for the OpenWeatherMap API
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    # API request URL
    url = f'{base_url}q={city}&appid={api_key}&units=metric'

    # Send GET request to the API
    response = requests.get(url)

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()

        # Extract relevant weather information
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']

        # Display weather information
        print(f'Weather in {city}:')
        print(f'Temperature: {temperature}°C')
        print(f'Humidity: {humidity}%')
        print(f'Wind Speed: {wind_speed} m/s')
        print(f'Description: {description}')
    else:
        print('Error fetching weather data. Please try again later.')

def main():
    # Prompt user for city name or zip code
    city = input('Enter city name: ')

    # Call get_weather function to retrieve weather information
    get_weather(city)

if __name__ == '__main__':
    main()
