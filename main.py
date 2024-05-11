import requests

url = "https://api.tomorrow.io/v4/weather/history/recent?location=47.65776895659352,-122.30736886136592&apikey=6PqY2SpuJYnsJngk52JhiV0uV1mO3pzq"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)