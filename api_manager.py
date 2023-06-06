import requests

class APIManager:
    def __init__(self, api_key):
        self.api_key = api_key

    def call_api(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise exception for non-2xx response codes

            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API call failed: {e}")
            return None

# Example usage
api_key = "6e2da7cf5b42dceb16bc2e85b3e16b3a"
manager = APIManager(api_key)

def get_weather_data(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response_data = manager.call_api(url)

    if response_data:
        # Process the API response data
        print(response_data['main']['temp'])


def send_email(title, content, url):
    #call email api to send
    pass

# Pass latitude and longitude as parameters
latitude = 13.5460432
longitude = 2.0783398
get_weather_data(latitude, longitude)
