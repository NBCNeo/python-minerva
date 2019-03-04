import requests
r = requests.get('https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=bfafd889c3fa59e19a74bfb26fccea48')
for i in range(3):
    print("{}: {}".format(r.json()['list'][i]['dt_txt'], r.json()['list'][i]['weather'][0]['description']))
