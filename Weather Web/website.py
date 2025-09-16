from flask import Flask, request, render_template, jsonify
import requests
from datetime import datetime
from collections import defaultdict
from datetime import datetime

app = Flask(__name__)

api_key = "a2305b483e74316e4ff11f03f0d854b6"


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/current", methods=["POST"])
def weather_function():
    ip_address = request.remote_addr
    if ip_address == "127.0.0.1":
        ip_address = "8.8.8.8"

    geo_url = f"http://ip-api.com/json/{ip_address}"
    geo_response = requests.get(geo_url).json() #location
    if geo_response["status"] != "success":
        return jsonify({"error": "Could not get Location"})

    lat, lon, city = geo_response["lat"], geo_response["lon"], geo_response["city"]

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    weather_data = requests.get(weather_url).json()

    updated_dt = datetime.fromtimestamp(weather_data["dt"])  

    return jsonify({
        "city": city,
        "temperature": weather_data["main"]["temp"],
        "feels_like": weather_data["main"]["feels_like"],
        "weather": weather_data["weather"][0]["main"],
        "description": weather_data["weather"][0]["description"],
        "humidity": weather_data["main"]["humidity"],
        "windspeed": weather_data["wind"]["speed"],
        "visibility": weather_data["visibility"],
        "temp_max": weather_data["main"]["temp_max"],
        "lastUpdateDate": updated_dt.strftime("%B %d, %Y"),
        "lastUpdateTime": updated_dt.strftime("%I:%M %p")
    })

@app.route("/forecast", methods=["POST"])
def forecastFunction():
    ip_address = request.remote_addr
    if ip_address == "127.0.0.1":
        ip_address = "8.8.8.8"

    geo_url = f"http://ip-api.com/json/{ip_address}"
    geo_response = requests.get(geo_url).json() #location
    if geo_response["status"] != "success":
        return jsonify({"error": "Could not get location"})
    
    lat, lon, city = geo_response["lat"], geo_response["lon"], geo_response["city"]
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    forecast_data = requests.get(forecast_url).json()
    
    daily_forecast = defaultdict(list)
    for entry in forecast_data["list"]:
        dt = datetime.strptime(entry["dt_txt"],"%Y-%m-%d %H:%M:%S")
        date_str = dt.date().isoformat()
        if date_str not in daily_forecast:
            daily_forecast[date_str] = entry
    
    five_days = []
    for i, (date_str, entry) in enumerate(daily_forecast.items()):
        if i >= 5:
            break

        five_days.append({
            "day": datetime.strptime(date_str, "%Y-%m-%d").strftime("%A"),  # Monday, Tuesday...
            "temp": entry["main"]["temp"],
            "feels_like": entry["main"]["feels_like"],
             "weather": entry["weather"][0]["main"],         # e.g. "Clouds"
            "description": entry["weather"][0]["description"],
            "icon": entry["weather"][0]["icon"]
        })
    
    return jsonify({
        "city": city,
        "forecast": five_days
    })

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)