from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_data(place, forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    # Get data for the specified number of days (8 data points per day)
    nr_values = forecast_days * 8           
    filtered_data = data["list"][:nr_values]  
            
    return filtered_data

if __name__ == '__main__':
    print(get_data(place = "London", forecast_days = 3, option = "Temperature"))