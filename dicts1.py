weather = {"city": "Москва","temperature": "20"}
print("city:", weather["city"])
weather["temperature"] = int(weather["temperature"]) - 5
weather["temperature"] = str(weather["temperature"])
print("weather:", weather)