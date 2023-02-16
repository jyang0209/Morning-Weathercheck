import requests
import smtplib
from email.message import EmailMessage
import time

api_key = "API key from Openweathermap"
city_name = "city name"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial"

response = requests.get(url).json()

temp = str(response['main']['temp'])
weather_condition = response['weather'][0]['main']
current_time = str(time.ctime())

def send_message(body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['to'] = to

    user = "your email address"
    msg['from'] = user
    password = "your email application PW"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

def message(time, weather, temp):
     return f"Time: {time} \nWeather Condition: {weather} \nTemperature (F): {temp}"

send_message(message(current_time, weather_condition, temp), "your carrier's SMS gateway domain")
