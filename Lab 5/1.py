import sys
import math
from functools import reduce
#1
def solve_everything(data):
    #1.1
    task1 = list(filter(lambda x: x<5,data))
    print(f"Задание 1.1: {task1}")
    #1.2
    task2 = list(map(lambda x: x/2,data))
    print(f"Задание 1.2: {task2}")
    #1.3
    task3 = list(map(lambda x: x/2,filter(lambda x: x>17,data)))
    print(f"Задание 1.3: {task3}")
    #1.4
    task4 = sum(map(lambda x: x**2,filter(lambda x: x%9 == 0, range(10,100))))
    print(f"Задание 1.4: {task4}")
#2
def factorials(n):
    res = 1
    for i in range(1,n+1):
        res *= i
        yield res
#3
def square_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield b**2
        a, b = b, a + b
#4
def russian_alphabet():
    for code in range(ord('А'), ord('Я') + 1):
        yield chr(code)

#5 в main

#6
def arithmetic_operation(operation):
    if operation == "+":
        return lambda x, y: x + y
    elif operation == "-":
        return lambda x, y: x - y
    elif operation == "*":
        return lambda x, y: x * y
    elif operation == "/":
        return lambda x, y: x / y
    else:
        return None
#7
def same_by(characteristic,objects):
    if not objects:
        return True
    first_char_value = characteristic(objects[0])
    return all(characteristic(obj) == first_char_value for obj in objects[1:])
#8
def print_operation_table(operation, num_rows =9 ,num_columns = 9):
    for row in range(1,num_rows +1):
        row_values = []
        for col in range(1,num_columns +1):
            result = operation(row,col)
            row_values.append(str(result))
        print("\t".join(row_values))
#9
def ask_password(login,password,success,failure):
    login = login.lower()
    password = password.lower()
    vowels_list = "aeiouy"
    login_consonants = "".join([c for c in login if c not in vowels_list])
    pwd_consonants = "".join([c for c in password if c not in vowels_list])
    pwd_vowels_count = len([c for c in password if c in vowels_list])
    vowels_ok = (pwd_vowels_count == 3)
    consonants_ok = (pwd_consonants == login_consonants)
    if vowels_ok and consonants_ok:
        success(login)
    elif not vowels_ok and not consonants_ok:
        failure(login, "Everything is wrong")
    elif not vowels_ok:
        failure(login, "Wrong number of vowels")
    else:
        failure(login, "Wrong consonants")
def main_pwd(login, password):
    def handle_success(user_login):
        print(f"Привет, {user_login}!")
    def handle_failure(user_login, error_msg):
        print(f"Кто-то пытался притвориться пользователем {user_login},"
              f"но в пароле допустили ошибку: {error_msg.upper()}")
    ask_password(login,password,handle_success,handle_failure)

#10-16 в main

#17
def check_password_17(func):
    correct_password = "qwerty"
    def wrapper(*args, **kwargs):
        user_input = input("Введите пароль для доступа к функции: ")
        if user_input == correct_password:
            return func(*args, **kwargs)
        else:
            print("Неверный пароль. Доступ запрещён.")
            return None
    return wrapper
@check_password_17
def get_secret_data():
    return "Секретные данные: 42"
@check_password_17
def say_hello(name):
    print(f"Привет, {name}!")
#18
def check_password_18(correct_password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_input = input(f"Введите пароль для доступа к функции {func.__name__}:")
            if user_input == correct_password:
                return func(*args, **kwargs)
            else:
                print("Неверный пароль. Доступ запрещён.")
                return None
        return wrapper
    return decorator
@check_password_18("mysecret")
def get_confidential_info():
    print("Конфиденциальная информация: 12345")
@check_password_18("secret123")
def make_burger(typeOfMeat, withOnion, withTomato):
    print(f"Готовим бургер с {typeOfMeat}. Лук: {withOnion}, Томаты: {withTomato}")
    return "Бургер готов!"
#19
def cached(func):
    cache = {}
    def wrapper(*args,**kwargs):
        key = (args, tuple(kwargs.items()))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper
@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
def main():
    #1
    print("Задание 1:")
    solve_everything([1,20,3,40])
    print("-------------------------------")
    #2
    print("Задание 2:")
    for f in factorials(7):
        print(f)
    print("-------------------------------")
    #3
    print("Задание 3:")
    n= 7
    for val in square_fibonacci(n):
        print(val, end=" ")
    print("\n-------------------------------")
    #4
    print("Задание 4:")
    for letter in russian_alphabet():
        print(letter, end=" ")
    print("\n-------------------------------")
    #5
    print("Задание 5:")
    russian_letters = (chr(code) for code in range(ord('а'), ord('я') + 1))
    for letter in russian_letters:
        print(letter, end=" ")
    print("\n-------------------------------")
    #6
    print("Задание 6:")
    operation = arithmetic_operation("+")
    print(operation(1, 4))
    minus = arithmetic_operation('-')
    print(minus(10, 3))
    print("-------------------------------")
    #7
    print("Задание 7:")
    values1 = [0, 2, 10, 6]
    if same_by(lambda x: x % 2, values1):
        print('same')
    else:
        print('different')
    values2 = [1, 2, 3, 4]
    if same_by(lambda x: x % 2, values2):
        print('same')
    else:
        print('different')
    empty_list = []
    if same_by(lambda x: x*2, empty_list):
        print('empty list is same')
    else:
        print('empty list is different')
    print("-------------------------------")
    #8
    print("Задание 8:")
    print("Таблица 9x9 (умножение):")
    print_operation_table(lambda x, y: x * y)
    print("\nТаблица 5x9 (умножение):")
    print_operation_table(lambda x, y: x * y, 5)
    print("-------------------------------")
    #9
    print("Задание 9:")
    print("Пример 1:")
    main_pwd("Anastasia", "nsyatos") 
    print("Пример 2:")
    main_pwd("eugene", "aanig")
    print("Пример 3:")
    ask_password("anastasia", "nsyatos", lambda login: print('super'),lambda login, err: print('bad'))
    print("-------------------------------")
    #10
    print("Задание 10: Введите слова через пробел:")
    words = input().split()
    sorted_words = sorted(words, key=str.lower)
    print("Отсортированные слова:")
    print(" ".join(sorted_words))
    print("-------------------------------")
    #11
    print("Задание 11:")
    print("Введите числа через пробел:")
    numbers = list(map(int,input().split()))
    result = sorted(numbers, key = abs, reverse=True)
    print("Отсортированные числа по модулю убывания:")
    print(*result)
    print("-------------------------------")
    #12
    print("Задание 12:")
    points = [(1,1),(-1,-1),(0,2),(2,0),(1,0),(0,1)]
    print("Исходные точки:")
    for p in points:
        print(p)
    sorted_points = sorted(points, key=lambda p: (p[0]**2 + p[1]**2,p[0],p[1]))
    print("Отсортированные точки:")
    for p in sorted_points:
        print(p)
    print("-------------------------------")
    #13
    print("Задание 5:")
    matrix = [
    [64, 33, 79, 56, 78, 70, 45, 71, 82, 3],
    [96, 27, 8, 36, 72, 14, 91, 10, 21, 65],
    [95, 28, 91, 23, 78, 38, 21, 50, 64, 37],
    [97, 54, 94, 6, 48, 17, 37, 19, 78, 58],
    [69, 58, 35, 1, 70, 24, 60, 17, 3, 11],
    [48, 9, 13, 23, 82, 49, 79, 55, 29, 53],
    [9, 2, 67, 90, 0, 17, 34, 55, 49, 63],
    [98, 98, 23, 71, 66, 57, 15, 94, 34, 81],
    [58, 37, 32, 29, 10, 19, 53, 46, 95, 19],
    [41, 24, 95, 47, 58, 17, 74, 69, 62, 4]
    ]
    print("Матрица c 0:")
    for row in matrix:
        print(row)
    print(any(0 in row for row in matrix))
    matrix1 = [
    [64, 33, 79, 56, 78, 70, 45, 71, 82, 3],
    [96, 27, 8, 36, 72, 14, 91, 10, 21, 65],
    [95, 28, 91, 23, 78, 38, 21, 50, 64, 37],
    [97, 54, 94, 6, 48, 17, 37, 19, 78, 58],
    [69, 58, 35, 1, 70, 24, 60, 17, 3, 11],
    [48, 9, 13, 23, 82, 49, 79, 55, 29, 53],
    [9, 2, 67, 90, 1, 17, 34, 55, 49, 63],
    [98, 98, 23, 71, 66, 57, 15, 94, 34, 81],
    [58, 37, 32, 29, 10, 19, 53, 46, 95, 19],
    [41, 24, 95, 47, 58, 17, 74, 69, 62, 4]
    ]
    print("Матрица без 0:")
    for row in matrix1:
        print(row)
    print(any(0 in row for row in matrix1))
    print("-------------------------------")
    #14
    print("Задание 14:")
    print("Введите строки текста (пустая строка для завершения):")
    words_list = []
    for line in sys.stdin:
        if not line.strip():
            break
        line_words = [word.strip(".,!?;:-") for word in line.split()]
        words_list.extend(line_words)
    first_occurrences = {}
    for index, word in enumerate(words_list):
        if word and word[0].isupper():
            if word not in first_occurrences:
                first_occurrences[word] = index
    sorted_keys = sorted(first_occurrences.keys())
    for word in sorted_keys:
        print(f"{first_occurrences[word]} - {word}")
    print("-------------------------------")
    #15
    print("Задание 15:")
    print("Введите строки текста (пустая строка для завершения):")
    lines = []
    for line in sys.stdin:
        if not line.strip():
            break
        lines.append(line.strip())
    if lines:
        min_string = reduce(lambda a, b: a if a <b else b,lines)
        print(f"Минимальная строка: {min_string}")
    print("-------------------------------")
    #16
    print("Задание 16:")
    print("Введите числа (пустая строка для завершения):")
    numbers =[]
    for line in sys.stdin:
        stripped = line.strip()
        if not stripped:
            break
        numbers.append(int(stripped))
    if numbers:
        total_gcd = reduce(math.gcd, numbers)
        print(f"Наибольший общий делитель: {total_gcd}")
    else:
        print("Нет чисел для обработки.")
    print("-------------------------------")
    #17
    print("Задание 17:")
    result = get_secret_data()
    if result:
        print(result)
    say_hello("Алексей")
    print("-------------------------------")
    #18
    print("Задание 18:")
    get_confidential_info()
    make_burger("говядина", withOnion=True, withTomato=False)
    print("-------------------------------")
    #19
    print("Задание 19:")
    print(f"Фибоначчи 10: {fib(10)}")
    print(f"Фибоначчи 50: {fib(50)}")
    print("-------------------------------")
if __name__ == "__main__":
    main()