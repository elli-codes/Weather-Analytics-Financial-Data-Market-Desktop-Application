# Weather-Analytics-Financial-Data-Desktop-Application

A desktop weather dashboard built with Python and Tkinter that combines current weather conditions, a seven-day temperature forecast, a live clock, and market price information in one graphical interface.

The application allows users to select a city, retrieve current weather data, visualize daily maximum and minimum temperatures, and view selected currency and gold market prices. The interface is designed with a custom background, weather icons, interactive text elements, and a separate window for temperature charts.

✨ Features:

🌤️ Current Weather
Select from a list of 30 Iranian cities.
Retrieve current weather information for the selected city.
Display temperature in Celsius.
Show weather conditions, humidity, feels-like temperature, and wind speed.
Convert wind speed from meters per second to kilometers per hour.
Display weather icons for clear, cloudy, and rainy conditions.
Refresh the displayed weather by selecting the Weather Status text.
📈 Seven-Day Temperature Forecast
Retrieve a seven-day forecast using the Open-Meteo API.
Automatically obtain the selected city's geographical coordinates through geocoding.
Plot daily maximum and minimum temperatures.
Display the forecast in a separate window.
Embed Matplotlib charts directly into the Tkinter application.

💱 Market Price Information:


Display selected market values obtained from the Navasan API, including:

US dollar selling price
Euro price
Gold coin price (sekkeh)
18-karat gold price (18ayar)

The code also retrieves USDT and Bitcoin values from the API response, although these values are not currently displayed in the interface.


🕒 Live Clock and Date:

Display the current system time.
Display the current system date.
Update the clock every second using Tkinter's after() method.


🌐 APIs Used:

1. OpenWeatherMap

Purpose: Retrieve current weather conditions for the selected city.

The application requests the current-weather endpoint using the selected city, the country code IR, and metric units.

Data displayed includes:

main.temp — current temperature
weather[0].description — weather description
main.humidity — relative humidity
main.feels_like — feels-like temperature
wind.speed — wind speed

Official website: https://openweathermap.org/api

2. Open-Meteo

Purpose: Retrieve the seven-day temperature forecast.

The application first uses Open-Meteo's geocoding service to obtain latitude and longitude for the selected city. It then requests daily maximum and minimum temperatures and weather codes.

The chart uses the following daily fields:

time
temperature_2m_max
temperature_2m_min

Official website: https://open-meteo.com/

3. Navasan

Purpose: Retrieve market price information.

The application reads the following response fields:

usd_sell
eur
sekkeh
18ayar
usdt
btc

The interface currently displays only the dollar, euro, coin, and 18-karat gold values.

API website: https://www.navasan.tech/

Availability, API access rules, and returned values depend on the external services.

📽️Working demo video:https://youtu.be/ljz0oN6YzXE
