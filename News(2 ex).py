import requests
import json 



key = "8c75d4fd23b14dfebc314ace940cf1c3"
q='ITMO'


response = requests.get(f'https://newsapi.org/v2/everything?q={q}&apiKey={key}')
results = json.loads(response.text)
for i in range(len(results['articles'])):
    print('#'*30)
    print(' ')
    print(results['articles'][i]['title'])
    print(results['articles'][i]['source']['name'])
    print(results['articles'][i]['author'])
    print(results['articles'][i]['description'])
    print(results['articles'][i]['url'])
    print(' ')