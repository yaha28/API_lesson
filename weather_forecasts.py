import requests
api_url = "http://weather.livedoor.com/forecast/webservice/json/v1"
payload = {"city" : "280010"}
weather_data = requests.get(api_url, params=payload).json()
for weather in weather_data["forecasts"]:
    print(weather["dateLabel"] + "の天気は" + weather["telop"])
    try:
        print("　明日の最高気温は" + weather["temperature"]["max"]["celsius"] + "度")
        print("　明日の最低気温は" + weather["temperature"]["min"]["celsius"] + "度")
    except:
        continue
    