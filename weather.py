import requests
import sqlite3

api_key = "b87f28f2c6d011dc157d12604844eeb1"
city = "Bangalore"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

data = response.json()

temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
weather = data["weather"][0]["description"]
city_name = data["name"]

print("\nWeather Data:")
print("City:", city_name)
print("Temperature:", temperature)
print("Humidity:", humidity)
print("Weather:", weather)

# connect to database
conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS weather_data (
    city TEXT,
    temperature REAL,
    humidity INTEGER,
    weather TEXT
)
""")

# insert data
cursor.execute("""
INSERT INTO weather_data (city, temperature, humidity, weather)
VALUES (?, ?, ?, ?)
""", (city_name, temperature, humidity, weather))

conn.commit()
conn.close()

print("\nData stored in database ✅")