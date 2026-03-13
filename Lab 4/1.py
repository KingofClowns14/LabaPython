#1
def num_1():
    my_list = [2, 10, 4, 18, 3, 25, 1, 17]
    print(f"Исходный список:для 1.1-.3 {my_list}")
    #1. Элементы меньше 5
    res1 = [x for x in my_list if x < 5]
    print(f"Элементы меньше 5 для 1.1: {res1}")
    #2 Элементы деленные на 2
    res2 = [x / 2 for x in my_list]
    print(f"Элементы деленные на 2 для 1.2: {res2}")
    #3 Элементы > 17, умноженные на 2
    res3 = [x * 2 for x in my_list if x > 17]
    print(f"Элементы > 17, умноженные на 2 для 1.3: {res3}")
    #4 Список квадратов от 0 до n 
    n = int(input("Введите число n для 1.4: "))
    res4 = [x ** 2 for x in range(n + 1)]
    print(f"Список квадратов от 0 до {n} для 1.4: {res4}")
    #5 Квадраты чисел,введенных в одну строку
    nums_5 = [int(x) for x in input("Введите числа для 1.5 (через пробел): ").split()]
    print(f"Квадраты чисел для 1.5: {[x ** 2 for x in nums_5]}")
    #6 Квадраты нечетных чисел, не оканчивающиеся на 9(решение в одну строку)
    print("Результат фильтрации для 1.6",*[sq for sq in [int(x)**2 for x in input("Введите числа для 1.6 (через пробел): ").split()] if sq % 2 != 0 and sq % 10 != 9])
#2
def num_2():
    input_data = input("Введите числа через пробел для №2: ").split()
    bars = map(lambda n: '*' * int(n), input_data)
    print('\n'.join(bars))
#3
def triangle(a,b,c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("Это треугольник")
    else:
        print("Это не треугольник")
#4
def distance(x1, y1, x2, y2):
    res =((x2-x1)**2 + (y2-y1)**2)**0.5
    return res
#5
def number_to_words(n):
    ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", 
             "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", 
            "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    if n<10:
        return ones[n]
    elif 10 <= n < 20:
        return teens[n - 10]
    else:
        ten_part = tens[n // 10]
        one_part = ones[n % 10]
        if one_part:
            return f"{ten_part} {one_part}"
        else:
            return ten_part
#6       
def bracket_check(test_string):
    balanace = 0
    for char in test_string:
        if char == '(':
            balanace += 1
        elif char == ')':
            balanace -= 1
        if balanace < 0:
            print("NO")
            return
    if balanace == 0:
        print("YES")
    else:
        print("NO")
#7
def palindrome_check(s):
    clean_s=s.lower().replace(" ","")
    if clean_s == clean_s[::-1]:
        return "Палиндром"
    else:
        return "Не палиндром"
#8    
def tic_tac_toe(field):
    for row in field:
        if row[0] == row[1] == row[2] != '-':
            print(f"{row[0]} win")
            return
    for col in range(3):
        if field[0][col] == field[1][col] == field[2][col] != '-':
            print(f"{field[0][col]} win")
            return
    if field[0][0] == field[1][1] == field[2][2] != '-':
        print(f"{field[0][0]} win")
        return
    if field[0][2] == field[1][1] == field[2][0] != '-':
        print(f"{field[0][2]} win")
        return
    print("Draw")
#9
last_message = None
def print_without_duplicates(message):
    global last_message
    if message != last_message:
        print(message)
        last_message = message
#10
friends_db = {}
def add_friends(name_of_person,list_of_friends):
    if name_of_person not in friends_db:
        friends_db[name_of_person] = set()
    for friend in list_of_friends:
        friends_db[name_of_person].add(friend)
def are_friends(name_of_person1,name_of_person2):
    if name_of_person1 in friends_db:
        return name_of_person2 in friends_db[name_of_person1]
    return False
def print_friends(name_of_person):
    if name_of_person in friends_db:
        sorted_friends = sorted(friends_db[name_of_person])
        print(" ".join(sorted_friends))
    else:
        print("")
#11
one = 5
two = 4
three = 0
def to_roman(n):
    roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
        (5, 'V'), (4, 'IV'), (1, 'I')]
    result = ""
    for value, symbol in roman_map:
        while n >= value:
            result += symbol
            n -= value
    return result
def roman():
    global one, two, three
    three = one + two
    r_one = to_roman(one)
    r_two = to_roman(two)
    r_three = to_roman(three)
    print(f"{r_one} + {r_two} = {r_three}")
#12
def demostratete_diff():
    # Одинаковый результат
    print("Тест с числами (int)")
    a=10
    b=a #b ссылается на тот же объект, что и a
    a=a+5
    print(f"a = a+5: a={a}, b={b}")#b не изменился, так как a теперь ссылается на новый объект
    x=10
    y= x #y ссылается на тот же объект, что и x
    x += 5
    print(f"x += 5: x={x}, y={y}")# Одинаковый результат, но разный способ достижения
    # Разный результат
    print("Тест со списками (list)")
    list_a = [1, 2]
    list_b = list_a #list_b ссылается на тот же объект, что и list_a
    print(f"До изменения: list_a id = {id(list_a)}, list_b id ={id(list_b)}")
    print(f"До изменения: list_a  = {list_a}, list_b = {list_b}")
    list_a = list_a + [3] #list_a теперь ссылается на новый объект
    print(f"После list_a = list_a + [3]: list_a id = {id(list_a)}, list_b id ={id(list_b)}")#list_b не изменился, так как list_a теперь ссылается на новый объект
    print(f"После изменения: list_a  = {list_a}, list_b = {list_b}")
    # value += addition
    list_x = [1, 2]
    list_y = list_x #list_y ссылается на тот же объект, что и list_x
    print(f"До изменения: list_x id = {id(list_x)}, list_y id ={id(list_y)}")
    print(f"До изменения: list_x  = {list_x}, list_y = {list_y}")
    list_x += [3] #list_x изменяется на месте, так как += для списков выполняет расширение существующего объекта
    print(f"После list_x += [3]: list_x id = {id(list_x)}, list_y id ={id(list_y)}")#list_y изменился, так как list_x изменяется на месте
    print(f"После изменения: list_x  = {list_x}, list_y = {list_y}")
#13
def demonstrate_sorting():
    original_list = [5, 2, 9, 1,]
    #Sorted (arr)
    new_list = sorted(original_list)#создает новый отсортированный список
    print(f"Original list: {original_list}")
    print(f"Sorted list (new): {new_list}")
    #list.sort()
    result = original_list.sort()#сортирует список на месте и возвращает None
    print(f"Result of sort(): {result}")
    print(f"Original list after sort(): {original_list}")
#14
def fixed():
    numbers = [2,5,7,7,8,4,1,6]
    # ИСПРАВЛЕНИЕ: создаем два РАЗНЫХ пустых списка.
    # Теперь у каждого списка свой адрес в памяти, и они независимы друг от друга.
    odd = []
    even = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    print(f"Нечетные числа: {odd}")
    print(f"Четные числа: {even}")
#15
fractal = []
def create_fractal():
    global fractal
    fractal= [0,None,None,2]
    fractal[1] = fractal
    fractal[2] = fractal
    print(fractal)
#16
def fixed_continue_fibonacci_sequence(sequence,n):
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence.append(next_element)
#17
def fixed_mirror(arr):
    mirrored_part = arr[::-1]
    arr.extend(mirrored_part)
#18
def from_string_to_list(string, container):
    for part in string.split():
        container.append(int(part))
#19
def  transpose(matrix):
    matrix[:]=[list(row) for row in zip(*matrix)]
    # zip(*matrix) берет строки и группирует элементы с одинаковыми индексами в кортежи.
    # Так первая строка становится первым столбцом и т.д.
    # [list(row) for ... ] превращает эти кортежи обратно в списки.
    # matrix[:] = ... обновляет исходный список "на месте".
#20
def swap(first, second):
    first[:], second[:] = second[:], first[:]

def main():
    # print("Тест для 1:")
    # num_1()
    # print("-------------------------")
    # print("Тест для 2:")
    # num_2()
    # print("-------------------------")    
    # #3
    # print("Тест для 3:")
    # triangle(1, 1, 2)
    # triangle(7, 6, 10)
    # triangle(20, 13, 17)
    # print("-------------------------")
    # #4
    # print("Тест для 4:")
    # print("Введите координаты для 4: ")
    # x1 = float(input("Введите x1 для 4: "))
    # x2 = float(input("Введите x2 для 4: "))
    # y1 = float(input("Введите y1 для 4: "))
    # y2 = float(input("Введите y2 для 4: "))
    # print(f"Расстояние между точками: {distance(x1, y1, x2, y2)}")
    # print("-------------------------")
    # #5
    # print("Тест для 5:")
    # print(number_to_words(4))
    # print(number_to_words(12))
    # print(number_to_words(42))
    # print(number_to_words(67))
    # print("-------------------------")
    # #6
    # print("Тест для 6:")
    # bracket_check("()")
    # bracket_check("(()((")
    # bracket_check("")
    # print("-------------------------")
    # #7
    # print("Тест для 7:")
    # print(palindrome_check("А роза упала на лапу Азора"))
    # print(palindrome_check("Палиндром"))
    # print("-------------------------")
    # #8
    # print("Тест для 8:")
    # data ="""0 - 0
    # x x x
    # 0 0 -"""
    # field = [line.split() for line in data.split('\n')]
    # tic_tac_toe(field)
    # print("-------------------------")
    # #9
    # print("Тест для 9:")
    # print_without_duplicates("Привет")
    # print_without_duplicates("Не могу до тебя дозвониться")
    # print_without_duplicates("Не могу до тебя дозвониться")
    # print_without_duplicates("Не могу до тебя дозвониться")
    # print_without_duplicates("Когда доедешь до дома")
    # print_without_duplicates("Ага, жду")
    # print_without_duplicates("Ага, жду")
    # print("-------------------------")
    # #10
    # print("Тест для 10:")
    # add_friends("Алла", ["Марина", "Иван"])
    # print(are_friends("Алла", "Мария"))
    # add_friends("Алла", ["Мария"])
    # print(are_friends("Алла", "Мария"))
    # print("-------------------------")
    # #11
    # print("Тест для 11:")
    # roman()
    # print("-------------------------")
    # #12
    # print("Тест для 12:")
    # demostratete_diff()
    # print("-------------------------")
    # #13
    # print("Тест для 13:")
    # demonstrate_sorting()
    # print("-------------------------")
    # #14
    # print("Тест для 14:")
    # fixed()
    # print("-------------------------")
    # #15
    # print("Тест для 15:")
    # create_fractal()
    # print("-------------------------")
    # #16
    # print("Тест для 16:")
    # sequence1=[1, 1]
    # fixed_continue_fibonacci_sequence(sequence1, 1)
    # print(f"Последовательность Фибоначчи: {sequence1}")
    # sequence2=[1, 1, 2, 3, 5]
    # fixed_continue_fibonacci_sequence(sequence2, 0)
    # print(f"Последовательность Фибоначчи: {sequence2}")
    # print("-------------------------")
    # #17
    # print("Тест для 17:")
    # arr1 =[1, 2]
    # fixed_mirror(arr1)
    # print(f"Массив после зеркального расширения: {arr1}")
    # arr2 =[1]
    # fixed_mirror(arr2)
    # print(f"Массив после зеркального расширения: {arr2}")
    # print("-------------------------")
    # #18
    # print("Тест для 18:")
    # a = [1, 2, 3]
    # from_string_to_list("1 3 99 52", a)
    # print(f"Список после добавления элементов из строки: {a}")
    # a = [77,'abc']
    # from_string_to_list("", a)
    # print(f"Список после добавления элементов из строки: {a}")
    # print("-------------------------")
    # #19
    # print("Тест для 19:")
    # matrix1 = [[1]]
    # transpose(matrix1)
    # print("Транспонированная матрица 1:")
    # for line in matrix1:
    #     print(*line)
    # matrix2 = [[1,2], [3,4]]
    # transpose(matrix2)
    # print("Транспонированная матрица 2:")
    # for line in matrix2:
    #     print(*line)
    # print("-------------------------")
    # #20
    # print("Тест для 20:")
    # first = [1, 2, 3]
    # second = [4, 5, 6]
    # first_content = first[:]
    # second_content = second[:]
    # swap(first, second)
    # print(first, second_content, first == second_content)
    # print(second, first_content, second == first_content)
    # first = [1, 2, 3]
    # second = [4, 5, 6, 7]
    # first_content = first[:]
    # second_content = second[:]
    # swap(first, second)
    # print(first, second_content, first == second_content)
    # print(second, first_content, second == first_content)
    # print("-------------------------")
if __name__ == "__main__":
    main()