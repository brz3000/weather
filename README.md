1. С помощью данного скрипта можно получить погоду через терминал путем API запроса к сайту  https://wttr.in.
2. Для работы должен быть установлен python3. А также необходимо установить библиотеку requests.
3. Библиотека requests устанавливается командой:
	```bash
	pip install requests
```
Если используется виртуальная среда необходимо воспользоваться командой:
```bash
pipenv install requests
```
4. По умолчанию скрипт выводит информацию для 3-х гео зон: Лондон, Аэропорт Шереметьево, Череповец. Для получения погоды для других гео зон, следует изменить справочник cities. Например cities = ["москва", "пермь", "рио-де-жанейро"]
