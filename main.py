import requests
cities = ["лондон", "шереметьево", "череповец"]
url_template = 'https://wttr.in/{}?nTqM&lang=ru'
for city in cities:
	url = url_template.format(city)
	response = requests.get(url)
	print (response.text)