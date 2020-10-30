# Weather App

Creating weather script
-----------------------
The script will provide weather information using data from openweathermap.org. In this script, we are using `requests` package to make web requests to weather data.

Create Virtualenv
-----------------
- First create virtualenv to host our app.
```
$ mkdir -p venv/weather
$ python3.9 -m venv venv/weather
```
- Activate virtualenv and start coding.
```
$ source ~/venvs/weather/bin/activate
(weather) $ pip install requests
(weather) $ export OWM_API_KEY=[YOUR API KEY]
```
- Deactivate virtualenv, once done with coding and testing.
```
(weather) $ deactivate
```