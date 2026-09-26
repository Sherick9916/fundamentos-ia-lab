import requests

def fetch_weather_data(lat, lon, start_date, end_date):
    """Obtiene datos históricos diarios de temperatura usando Open-Meteo API."""
    url = f"https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_mean&timezone=America%2FBogota"
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error de red: {response.status_code}")