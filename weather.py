
import requests

def getWeather():

	url = 'http://api.openweathermap.org/data/2.5/weather?q=Seoul,KR&appid=b20a9613d403c280ae63deff646dbc29'
	resp = requests.get(url)
	if resp.status_code != 200:
    # This means something went wrong.
	    raise ApiError('GET /weather/ {}'.format(resp.status_code))	
	    return None

	data = resp.json()
	city = str(data['name'])
	weather = str(data['weather'][0]['main'])
	humidity = str(data['main']['humidity']) + '%'
	K = 273
	temp = str(data['main']['temp'] - K)
	temp_max = str(data['main']['temp_max'] - K)
	temp_min = str(data['main']['temp_min'] - K)
	
	return [city, weather, humidity, temp, temp_max, temp_min]



print(getWeather())
