import requests


cities = ["лондон", "шереметьево", "череповец"]
url_template = 'https://wttr.in/{}'
params = {
    "nTqM": "",
    "lang": "ru"
}


def main():
    for city in cities:
        url = url_template.format(city)
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print(response.text)
        else:
            pass


if __name__ == '__main__':
    main()
