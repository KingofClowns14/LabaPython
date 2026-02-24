def number_1():
    s = input("Enter a string Task_1: ")
    print(s[2])#третий символ строки
    print(s[-2])#предпоследний символ строки
    print(s[:5])#первые пять символов строки
    print(s[:-2])#вся строка, кроме последних двух символов
    print(s[::2])#все символы с четными индексами
    print(s[1::2])#все символы с нечетными индексами
    print(s[::-1])#все символы в обратном порядке
    print(s[::-2])#все символы в обратном порядке через один
    print(len(s))#длина строки
def number_2():
    s = input("Enter a string Task_2: ")
    middle = (len(s) - 1) // 2
    firs_half = s[:middle]
    second_half = s[middle:]
    new_string = second_half + firs_half
    print(new_string)
def number_3():
    s = "hello world it is high time"
    first = s.find('h')
    last = s.rfind('h')
    # Часть до первого h включительно s[:first+1]
    # Часть между ними в обратном порядке s[first+1:last][::-1]
    # Часть после последнего h s[last:]
    result = s[:first+1] + s[first+1:last][::-1] + s[last:]
    print(result)
def number_4():
    s = "potatoff"
    f_count = s.count('f')
    if f_count == 1:
        print(s.find('f'))
    elif f_count >= 2:
        print(s.find('f'), s.rfind('f'))
def number_5():
    first_word = input("Enter a first word Task_5: ")
    while True:
        current_word = input("Enter a second word Task_5: ")
        if current_word[0] != first_word[-1]:
            print(current_word)
            break
        first_word = current_word
def number_6():
    s = input("Enter a string Task_6: ")
    result = ""
    # enumerate(word) дает нам индекс (i) и саму букву (char)
    # Индексация начинается с 0, поэтому для "номера в строке" прибавляем 1
    for i,char in enumerate(s):
        result += char * (i + 1)
    print(result)
def number_7():
    s = input("Enter a string Task_7: ")
    char = s[0]
    commands = s[1:]
    current_x = 0
    line_indices = {current_x}
    def print_row(indices):
        max_idx = max(indices)
        row = [' '] * (max_idx + 1)
        for idx in indices:
            row[idx] = char
        print(''.join(row))
    for cmd in commands:
        if cmd == 'v':
            print_row(line_indices)
            line_indices = {current_x}
        elif cmd == '>':
            current_x += 1
            line_indices.add(current_x)
        elif cmd == '<':
            current_x -= 1
            line_indices.add(current_x)
    print_row(line_indices)
def number_8():
    s = input("Enter a string Task_8: ")
    n = len(s)
    num_rows = ( n + 1) // 2
    for i in range(num_rows):
        left_idx = (n-1) // 2 - i
        right_idx = n // 2 + i
        leading_spaces = ' ' * left_idx
        if left_idx == right_idx:
            print(leading_spaces + s[left_idx])
        else:
            middle_spaces_count = right_idx - left_idx - 1
            middle_spaces = ' ' * middle_spaces_count
            print(leading_spaces + s[left_idx] + middle_spaces + s[right_idx])
def number_9():
    numbers = list(map(int, input("Enter a list of numbers Task_9: ").split()))
    for i in range(1,len(numbers)):
        if numbers[i] > numbers[i-1]:
            print(numbers[i], end=' ')
def number_10():
    numbers = list(map(int, input("Enter a list of numbers Task_10: ").split()))
    for i in range(1,len(numbers)):
        if numbers[i-1] * numbers[i] > 0:
            print(numbers[i-1],numbers[i])
            break
def number_11():
    a = list(map(int, input("Enter a list of numbers Task_11: ").split()))
    for i in range(0, len(a) -1,2):
        a[i],a[i+1] = a[i+1],a[i]
    print(*a)
def number_12():
    a = input("Enter a list of numbers Task_12: ").split()
    for x in a:
        if a.count(x) == 1:
            print(x,end = ' ')
def number_13():
    indices = list(map(int, input("Enter a list of indices Task_13: ").split()))
    source_words = input("Enter a list of words Task_13: ").split()
    new_words = []
    for i in indices:
        word = source_words[i-1].lower()
        new_words.append(word)
    result_string = " ".join(new_words)
    print(result_string.capitalize())
def number_14():
    x =[]
    y =[]
    for i in range(8):
        coords = list(map(int, input("Enter coordinates Task_14 (x y): ").split()))
        x.append(coords[0])
        y.append(coords[1])
    attack = False
    for i in range(8):
        for j in range(i+1,8):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                attack = True
                break
        if attack:
            break
    if attack:
        print("YES")
    else:
        print("NO")
def number_15():
    try:
        n =int(input("Enter a positive integer Task_15: "))
    except (ValueError,EOFError):
        return
    queue = []
    for _ in range(n):
        line = input().strip()
        if line == "Следующий!":
            if queue:
                patient = queue.pop(0)
                print(f"Заходит {patient}!")
            else:
                print("В очереди никого нет!")
        else:
            name = line.split(" - ")[1].rstrip('.')
            if "Кто последний?" in line:
               queue.append(name)
            elif "Я только спросить!" in line:
                queue.insert(0,name)
def main():
    number_1()
    number_2()
    number_3()
    number_4()
    number_5()
    number_6()
    number_7()
    number_8()
    number_9()
    number_10()
    number_11()
    number_12()
    number_13()
    number_14()
    number_15()
if __name__ == "__main__":
    main()