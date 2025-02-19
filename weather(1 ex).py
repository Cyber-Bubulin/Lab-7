import requests 
import json


city = "Sarov"

key = '34d5a145f0c824b4612cb1120ae6d480'
response = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}')
results = json.loads(response.text)

data_main = {
    'Город': f'{city}',
    "Температура (°С) ": int(results['main']['temp']) - 273,
    'Влажность (%)': results['main']['humidity'], 
    "Давление (кПа)": results['main']['pressure']

}
print(data_main)