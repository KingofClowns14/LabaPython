import requests
import os
import requests
from dotenv import load_dotenv
import math
from bs4 import BeautifulSoup
from urllib.parse import urljoin # Для правильной склейки ссылок
from collections import Counter
import random
from urllib.parse import urljoin
import urllib3

# Загружаем путь к текущему файлу, чтобы точно найти .env
dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
load_dotenv(dotenv_path)

# Глобальная переменная API-ключа
API_KEY = os.getenv("YANDEX_API_KEY")
BASE_URL = "https://geocode-maps.yandex.ru/1.x/"
STATIC_URL = "https://static-maps.yandex.ru/1.x/" # Для карт и снимков

#1

# ll — координаты центра карты (долгота и широта через запятую).
# spn — протяженность области показа в градусах (чем меньше значения, тем «ближе» карта).
# l — тип карты (map для схемы, sat для спутника).
# a) Крупномасштабную схему с КемГУ 
# https://static-maps.yandex.ru/1.x/?ll=86.090811,55.351805&spn=0.002,0.002&l=map 
# b) Крупномасштабную схему района, в котором вы живете 
# https://static-maps.yandex.ru/1.x/?ll=86.168271,55.341338&spn=0.005,0.005&l=map
# c) Крупномасштабную схему города, в котором вы родились 
# https://static-maps.yandex.ru/1.x/?ll=86.086029,55.355790&spn=0.2,0.2&l=map
# d) Спутниковый снимок Эйфелевой башни
# https://static-maps.yandex.ru/1.x/?ll=2.2945,48.8584&spn=0.002,0.002&l=sat
# e) Спутниковый снимок Авачинского вулкана 
# https://static-maps.yandex.ru/1.x/?ll=158.833,53.255&spn=0.1,0.1&l=sat
# f) Спутниковый снимок озера Байкал 
# https://static-maps.yandex.ru/1.x/?ll=108.0,53.5&spn=10.0,5.0&l=sat
# g) Спутниковый снимок космодрома Байконур
# https://static-maps.yandex.ru/1.x/?ll=63.344341,45.924479&spn=0.02,0.02&l=sat

# 2
def get_geocoder_data(address):
    # Общая функция для выполнения запроса к API
    if not API_KEY:
        print("Ошибка: API_KEY не найден в .env файле!")
        return None
    params = {
        "apikey": API_KEY,
        "geocode": address,
        "format": "json"
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status() # Проверка на ошибки HTTP
        return response.json()
    except Exception as e:
        print(f"Ошибка при запросе к API ({address}): {e}")
        return None
    
def get_coords(json_data):
    # Извлекает долготу и широту из JSON ответа
    try:
        pos = json_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        lon, lat = map(float, pos.split())
        return lon, lat
    except (KeyError, IndexError, TypeError):
        return None, None
    
def task_a():
    print("\nЗадача A: Кто севернее?")
    data_y = get_geocoder_data("Якутск")
    data_m = get_geocoder_data("Магадан")
    _, lat_y = get_coords(data_y)
    _, lat_m = get_coords(data_m)
    if lat_y and lat_m:
        print(f"Широта Якутска: {lat_y}")
        print(f"Широта Магадана: {lat_m}")
        result = "Якутск" if lat_y > lat_m else "Магадан"
        print(f"Ответ: {result} находится севернее.")

def task_b(home_city="Кемерово"):
    print(f"\nЗадача B: Кто южнее ({home_city} или Торонто)?")
    data_h = get_geocoder_data(home_city)
    data_t = get_geocoder_data("Торонто")
    _, lat_h = get_coords(data_h)
    _, lat_t = get_coords(data_t)
    if lat_h and lat_t:
        print(f"Широта {home_city}: {lat_h}")
        print(f"Широта Торонто: {lat_t}")
        result = home_city if lat_h < lat_t else "Торонто"
        print(f"Ответ: {result} находится южнее.")

def task_c(home_city="Кемерово"):
    print("\nЗадача C: Федеральные округа")
    cities = ["Хабаровск", "Уфа", "Нижний Новгород", "Калининград", home_city]
    for city in cities:
        data = get_geocoder_data(city)
        try:
            # Ищем компонент адреса с типом 'admin_level_2' (обычно федеральный округ в РФ)
            components = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components']
            district = "Не определен"
            for comp in components:
                if "округ" in comp['name'].lower():
                    district = comp['name']
                    break
            print(f"Город {city} относится к: {district}")
        except:
            print(f"Город {city}: данные не найдены.")

def task_d():
    print("\nЗадача D: Почтовый индекс КемГУ")
    data = get_geocoder_data("Кемерово, ул. Красная, 6")
    try:
        address_meta = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']
        postal_code = address_meta.get('postal_code', 'Индекс не указан')
        print(f"Почтовый индекс КемГУ: {postal_code}")
    except:
        print("Данные по КемГУ не получены.")
#3
def print_museum_info():
    address = "Москва, Красная площадь, 1"
    params = {
        "apikey": API_KEY,
        "geocode": address,
        "format": "json"
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        # Получаем первый найденный объект
        geo_object = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
        # 1. Извлекаем полный адрес
        full_address = geo_object['metaDataProperty']['GeocoderMetaData']['text']
        # 2. Извлекаем координаты
        coords = geo_object['Point']['pos']
        print(f"Исторический музей")
        print(f"Полный адрес: {full_address}")
        print(f"Координаты: {coords}")
    except Exception as e:
        print(f"Не удалось получить данные: {e}")
#4
def task_city_regions():
    cities = ["Барнаул", "Мелеуз", "Йошкар-Ола"]
    print("\nЗадание: Определение областей")
    for city in cities:
        params = {
            "apikey": API_KEY,
            "geocode": city,
            "format": "json"
        }
        try:
            response = requests.get(BASE_URL, params=params)
            data = response.json()
            components = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components']
            region = "Регион не найден"
            for comp in components:
                # Ищем province, но ИГНОРИРУЕМ те, где написано "федеральный округ"
                if comp['kind'] == 'province' and "федеральный округ" not in comp['name'].lower():
                    region = comp['name']
                    break
            print(f"Город {city} относится к: {region}")
        except Exception as e:
            print(f"Ошибка при запросе города {city}: {e}")
#5
def task_mur_postal_code():
    # Адрес Петровки, 38 в Москве
    address = "Москва, Петровка, 38"
    print("\n-Задание: Почтовый индекс МУРа")
    params = {
        "apikey": API_KEY,
        "geocode": address,
        "format": "json"
    }
    try:
        # Используем глобальную переменную BASE_URL
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        # Путь в JSON: GeoObject -> metaDataProperty -> GeocoderMetaData -> Address
        geo_object = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
        address_data = geo_object['metaDataProperty']['GeocoderMetaData']['Address']
        # Извлекаем индекс
        index = address_data.get('postal_code', 'Индекс не найден')
        print(f"Объект: Московский Уголовный Розыск (Петровка, 38)")
        print(f"Почтовый индекс: {index}")
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")
#6
def task_australia():
    print("\nЗагрузка снимка Австралии")
    # Параметры: l=sat (спутник), ll=центр, z=масштаб, size=размер
    params = {
        "l": "sat",
        "ll": "135.0,-25.0",
        "z": "4",
        "size": "650,450"
    }
    try:
        response = requests.get(STATIC_URL, params=params)
        if response.status_code == 200:
            with open("australia_free.png", "wb") as f:
                f.write(response.content)
            print("Успешно сохранено в australia.png")
        else:
            print(f"Ошибка {response.status_code}.") 
    except Exception as e:
        print(f"Ошибка: {e}")
#7
def task_kemerovo_map():
    print("\nЗадание: Карта Кемерово с метками")
    places = [
        "Кемерово, проспект Кузнецкий, 79",   # ЖД Вокзал
        "Кемерово, Сосновый бульвар, 6",      # Кардиологический диспансер
        "Кемерово, ул. Красная Горка, 17",    # Музей Красная Горка
        "Кемерово, парк Ангелов"              # Парк Ангелов
    ]
    # pmwtm (белая) ЖД Вокзал, 
    # pmrdm (красная) Кардиологический диспансер, 
    # pmblm (синяя) Музей Красная Горка, 
    # pmgnm (зеленая) Парк Ангелов
    styles = ["pmwtm", "pmrdm", "pmblm", "pmgnm"]
    points = []
    # 1. Получаем координаты
    for place in places:
        params = {"apikey": API_KEY, "geocode": place, "format": "json"}
        try:
            res = requests.get(BASE_URL, params=params).json()
            members = res['response']['GeoObjectCollection']['featureMember']
            if members:
                pos = members[0]['GeoObject']['Point']['pos']
                clean_pos = pos.strip().replace(" ", ",")
                points.append(clean_pos)
        except Exception as e:
            print(f"Ошибка поиска {place}: {e}")
    if not points:
        print("Отмена: Точки не найдены.")
        return
    pt_parts = []
    for i in range(len(points)):
        # Берем стиль из нашего списка
        pt_parts.append(f"{points[i]},{styles[i]}")
    pt_param = "~".join(pt_parts)
    # 3. Запрос к Static API
    static_params = {
        "l": "map",
        "pt": pt_param,
        "size": "600,450"
    }
    try:
        response = requests.get(STATIC_URL, params=static_params)
        if response.status_code == 200:
            with open("kemerovo_map.png", "wb") as f:
                f.write(response.content)
            print("Успех! Карта сохранена: kemerovo_map.png")
        else:
            print(f"Ошибка: {response.status_code}")
            print(f"Текст ошибки: {response.text}")
    except Exception as e:
        print(f"Ошибка: {e}")
#8
def task_kuzbass_route():
    print("\nЗадание: Маршрут по Кемеровской области")
    # 1. Список городов маршрута
    cities = ["Кемерово", "Ленинск-Кузнецкий", "Новокузнецк", "Шерегеш"]
    coords_list = []
    # 2. Получаем координаты через Геокодер
    for city in cities:
        params = {"apikey": API_KEY, "geocode": city, "format": "json"}
        try:
            res = requests.get(BASE_URL, params=params).json()
            pos = res['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
            # Меняем пробел на запятую
            coords_list.append(pos.replace(" ", ","))
        except Exception as e:
            print(f"Ошибка поиска города {city}: {e}")
    if len(coords_list) < 2:
        print("Недостаточно точек для построения маршрута.")
        return
    # 3. Формируем параметр pl (линия)
    # Цвет: 0000ffff (синий), Толщина: 5
    line_style = "c:0000ffff,w:4"
    all_points = ",".join(coords_list)
    pl_param = f"{line_style},{all_points}"
    static_params = {
        "l": "map",
        "pl": pl_param,   # Параметр для линии
        "size": "650,450"
    }
    try:
        response = requests.get(STATIC_URL, params=static_params)
        if response.status_code == 200:
            with open("kuzbass_route.png", "wb") as f:
                f.write(response.content)
            print("Карта с маршрутом сохранена: kuzbass_route.png")
        else:
            print(f"Ошибка Static API: {response.status_code}")
            print(f"Причина: {response.text}")
    except Exception as e:
        print(f"Ошибка: {e}")
#9
def task_southernmost_city():
    print("\nЗадание: Самый южный город")
    # 1. Ввод списка городов с клавиатуры
    input_str = input("Введите список городов через запятую: ")
    # Очищаем от лишних пробелов и создаем список
    cities = [city.strip() for city in input_str.split(",") if city.strip()]
    if not cities:
        print("Список пуст.")
        return
    southernmost_city = None
    min_lat = 90.0 # Начальное значение (Северный полюс)
    # 2. Перебор городов и поиск минимальной широты
    for city in cities:
        params = {
            "apikey": API_KEY,
            "geocode": city,
            "format": "json"
        }
        try:
            response = requests.get(BASE_URL, params=params)
            data = response.json()
            # Извлекаем координаты
            pos = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
            lat = float(pos.split()[1]) # Широта — это второе число
            print(f"Город {city}: широта {lat}")
            # Сравниваем: чем меньше широта, тем южнее город
            if lat < min_lat:
                min_lat = lat
                southernmost_city = city
        except Exception:
            print(f"Не удалось найти координаты города: {city}")
    # 3. Печать результата
    if southernmost_city:
        print(f"\nОтвет: Самым южным из списка является город {southernmost_city}.")
#10 
def calculate_distance(p1, p2):
    # Рассчитывает расстояние между двумя точками (lon, lat) в километрах
    # p1 и p2 это кортежи (lon, lat)
    lon1, lat1 = p1
    lon2, lat2 = p2
    radius = 6371  # Радиус Земли в км
    # Переводим в радианы
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius * c

def task_path_info():
    print("\nЗадание: Длина пути и карта с меткой в центре")
    # 1. Задаем точки (например: Москва, Тула, Рязань)
    locations = ["Москва", "Тула", "Рязань"]
    coords = []
    # Получаем координаты точек через Геокодер
    for loc in locations:
        params = {"apikey": API_KEY, "geocode": loc, "format": "json"}
        try:
            res = requests.get(BASE_URL, params=params).json()
            pos = res['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
            lon, lat = map(float, pos.split())
            coords.append((lon, lat))
        except:
            print(f"Ошибка поиска: {loc}")
    if len(coords) < 2: return
    # 2. Определяем общую длину пути
    total_dist = 0
    for i in range(len(coords) - 1):
        total_dist += calculate_distance(coords[i], coords[i+1])
    print(f"Путь: {' -> '.join(locations)}")
    print(f"Общая длина пути: {total_dist:.2f} км")
    # 3. Находим среднюю точку последовательности для метки
    # (Берем средний индекс в списке)
    mid_idx = len(coords) // 2
    mid_point = coords[mid_idx]
    # 4. Формируем параметры для карты
    # Подготовка строк координат
    pts_str = ",".join([f"{c[0]},{c[1]}" for c in coords])
    static_params = {
        "l": "map",
        "pl": f"c:ff0000ff,w:5,{pts_str}",  # Ломаная линия (красная)
        "pt": f"{mid_point[0]},{mid_point[1]},pm2rdm", # Метка в средней точке
        "size": "650,450"
    }
    # 5. Сохраняем карту
    try:
        response = requests.get(STATIC_URL, params=static_params)
        if response.status_code == 200:
            with open("path_map.png", "wb") as f:
                f.write(response.content)
            print("Карта пути сохранена в файл: path_map.png")
        else:
            print(f"Ошибка карты: {response.status_code}")
    except Exception as e:
        print(f"Ошибка: {e}")

#11
def task_extract_links():
    print("\nЗадание: Извлечение ссылок с сайта")
    url = "http://olympus.realpython.org/profiles"
    base_domain = "http://olympus.realpython.org"
    try:
        # 1. Получаем содержимое страницы
        response = requests.get(url)
        response.raise_for_status()
        # 2. Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        # 3. Находим все теги <a>
        links = soup.find_all('a')
        # 4. Перебираем их и выводим атрибут href
        for link in links:
            href = link.get('href')
            if href:
                # urljoin автоматически склеит домен и путь, 
                # превратив /profiles/aphrodite в полную ссылку
                full_url = urljoin(base_domain, href)
                print(full_url) 
    except Exception as e:
        print(f"Ошибка при парсинге страницы: {e}")

#12
def task_top_authors():
    print("\nЗадание: Топ авторов по количеству цитат")
    base_url = "https://quotes.toscrape.com"
    current_page = "/page/1/"
    all_authors = []
    print("Сбор данных с сайта (это может занять несколько секунд)...")
    while current_page:
        try:
            # 1. Загружаем страницу
            response = requests.get(base_url + current_page)
            soup = BeautifulSoup(response.text, 'html.parser')
            # 2. Находим всех авторов на текущей странице
            # Имена авторов лежат в тегах <small> с классом "author"
            authors_on_page = soup.find_all('small', class_='author')
            for author in authors_on_page:
                all_authors.append(author.get_text())
            # 3. Ищем ссылку на следующую страницу
            next_button = soup.find('li', class_='next')
            if next_button:
                current_page = next_button.find('a')['href']
            else:
                current_page = None  # Больше страниц нет
        except Exception as e:
            print(f"Ошибка при парсинге: {e}")
            break
    # 4. Подсчитываем количество цитат для каждого автора
    # Counter создаст словарь вида {'Автор': количество}
    author_counts = Counter(all_authors)
    # 5. Сортируем: .most_common() сразу возвращает список, отсортированный по убыванию
    sorted_authors = author_counts.most_common()
    # 6. Вывод результата
    print(f"\nВсего найдено авторов: {len(author_counts)}")
    print(f"{'Автор':<30} | {'Цитат':<5}")
    print("-" * 40)
    for author, count in sorted_authors:
        print(f"{author:<30} | {count:<5}")
#13
def task_random_quotes():
    print("\nЗадание: Пять случайных цитат")
    base_url = "https://quotes.toscrape.com"
    current_page = "/page/1/"
    all_quotes = []
    print("Собираем цитаты со всех страниц (всего их 10)...")
    while current_page:
        try:
            response = requests.get(base_url + current_page)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Находим блоки с цитатами
            quote_elements = soup.find_all('div', class_='quote')
            for elem in quote_elements:
                text = elem.find('span', class_='text').get_text()
                author = elem.find('small', class_='author').get_text()
                all_quotes.append(f"{text} (Автор: {author})")
            # Ищем кнопку "Next" для перехода на следующую страницу
            next_button = soup.find('li', class_='next')
            current_page = next_button.find('a')['href'] if next_button else None
        except Exception as e:
            print(f"Ошибка при сборе данных: {e}")
            break
    # Проверяем, удалось ли собрать цитаты
    if len(all_quotes) >= 5:
        # Выбираем 5 уникальных случайных элементов из списка
        random_five = random.sample(all_quotes, 5)
        print("\nВот 5 случайных цитат для вас:")
        print("-" * 50)
        for i, quote in enumerate(random_five, 1):
            print(f"{i}. {quote}\n")
    else:
        print("Не удалось собрать достаточное количество цитат.")
#14
def task_quotes_by_tags():
    print("\nЗадание: Поиск цитат по тегам")
    # 1. Принимаем теги от пользователя
    user_input = input("Введите теги через пробел (например, love life music): ")
    # Превращаем ввод в множество (set) для быстрого сравнения
    target_tags = set(user_input.lower().split())
    if not target_tags:
        print("Вы не ввели ни одного тега.")
        return
    base_url = "https://quotes.toscrape.com"
    current_page = "/page/1/"
    found_count = 0
    print(f"Начинаю поиск цитат с тегами: {', '.join(target_tags)}...")
    # 2. Проходим по всем страницам сайта
    while current_page:
        try:
            response = requests.get(base_url + current_page)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Находим все блоки цитат на текущей странице
            quote_blocks = soup.find_all('div', class_='quote')
            for block in quote_blocks:
                # Извлекаем все теги этой конкретной цитаты
                tags_in_quote = {tag.get_text().lower() for tag in block.find_all('a', class_='tag')}
                # Проверяем, есть ли пересечение между тегами пользователя и тегами цитаты
                # Если хотя бы один тег совпал, выводим цитату
                if target_tags & tags_in_quote:
                    text = block.find('span', class_='text').get_text()
                    author = block.find('small', class_='author').get_text()
                    print(f"\nЦитата: {text}")
                    print(f"Автор: {author} | Теги: {', '.join(tags_in_quote)}")
                    found_count += 1
            # Переход на следующую страницу
            next_button = soup.find('li', class_='next')
            current_page = next_button.find('a')['href'] if next_button else None
        except Exception as e:
            print(f"Произошла ошибка при поиске: {e}")
            break
    # 3. Итог поиска
    if found_count == 0:
        print("\nЦитат с такими тегами не найдено на всем сайте.")
    else:
        print(f"\nПоиск завершен. Найдено цитат: {found_count}")
def main():
    #2
    print("Запуск программы Геокодер...")
    my_city = "Кемерово" 
    task_a()
    task_b(my_city)
    task_c(my_city)
    task_d()
    print("\nПрограмма завершена.")
    print("----------------------")
    # 3
    print_museum_info()
    print("----------------------")
    #4
    task_city_regions()
    print("----------------------")
    #5
    task_mur_postal_code()
    print("----------------------")
    # 6
    task_australia()
    print("----------------------")
    #7
    task_kemerovo_map()
    print("----------------------")
    #8
    task_kuzbass_route()
    print("----------------------")
    #9
    task_southernmost_city()
    print("----------------------")
    #10
    task_path_info()
    print("----------------------")
    #11
    task_extract_links()
    print("----------------------")
    #12
    task_top_authors()
    print("----------------------")
    #13
    task_random_quotes()
    print("----------------------")
    #14
    task_quotes_by_tags()
    print("----------------------")
if __name__ == "__main__":
    main()
