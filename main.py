import requests

print("meow?")

def getChicagoPrayerTimes():
    response = requests.get("https://api.aladhan.com/v1/timingsByCity?city=Chicago&country=USA&method=2")
    return response.json()

if __name__ == "__main__":
    response = getChicagoPrayerTimes()
    
    data = response["data"]
    timingsForLondon = data["timings"]
    print(timingsForLondon)
    print("test worked")
