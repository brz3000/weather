import requests


cities = ["лондон", "шереметьево", "череповец"]
url_template = 'https://wttr.in/{}'
params = {"nTqM-10": "",
          "lang": "ru"}


def main():
    for city in cities:
        url = url_template.format(city)
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            print(response.text)
        except requests.ConnectionError:
            print("Не удалось выполнить запрос. Ошибка соединения")


if __name__ == '__main__':
    main()
