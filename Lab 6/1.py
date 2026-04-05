import math
import sys
#1
class BigBell:
    def __init__(self):
        self.is_ding = True
    def sound(self):
        if self.is_ding:
            print("Ding")
        else:
            print("Dong")
        self.is_ding = not self.is_ding
#2
class Balance:
    def __init__(self):
        self.left_weight = 0
        self.right_weight = 0
    def add_left(self, weight):
        self.left_weight += weight
    def add_right(self, weight):
        self.right_weight += weight
    def result(self):
        if self.left_weight == self.right_weight:
            return "="
        elif self.left_weight > self.right_weight:
            return "L"
        else:
            return "R"
#3
class Selector:
    def __init__(self, numbers):
        self.numbers = numbers
    def get_odds(self):
        return [x for x in self.numbers if x % 2 != 0]
    def get_evens(self):
        return [x for x in self.numbers if x % 2 == 0]
#4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y
    def __ne__(self, other):
        return not self.__eq__(other)
#5
class ReversedList:
    def __init__(self, lst):
        self.lst = lst
    def __len__(self):
        return len(self.lst)
    def __getitem__(self, index):
        return self.lst[-1 - index]
#6
class SparseArray:
    def __init__(self):
        self.data = {}
    def __setitem__(self, index, value):
        if value == 0:
            if index in self.data:
                del self.data[index]
        else:
            self.data[index] = value
    def __getitem__(self, index):
        return self.data.get(index, 0)
#7
class Polynomial:
    def __init__(self, coefficients):
        self.coeffs = list(coefficients)
    def __call__(self, x):
        res = 0
        for i, c in enumerate(self.coeffs):
            res += c * (x ** i)
        return res
    def __add__(self, other):
        len1 = len(self.coeffs)
        len2 = len(other.coeffs)
        max_len = max(len1, len2)
        new_coeffs = []
        for i in range(max_len):
            c1 = self.coeffs[i] if i < len1 else 0
            c2 = other.coeffs[i] if i < len2 else 0
            new_coeffs.append(c1 + c2)
        return Polynomial(new_coeffs)
#8
class Queue:
    def __init__(self, *values):
        self.items = list(values)
    def append(self, *values):
        self.items.extend(values)
    def copy(self):
        return Queue(*self.items)
    def pop(self):
        if not self.items:
            return None
        return self.items.pop(0)
    def extend(self, other):
        self.items.extend(other.items)
    def next(self):
        return Queue(*self.items[1:])
    def __add__(self, other):
        return Queue(*(self.items + other.items))
    def __iadd__(self, other):
        self.extend(other)
        return self
    def __eq__(self, other):
        if not isinstance(other, Queue):
            return False
        return self.items == other.items
    def __rshift__(self, n):
        return Queue(*self.items[n:])
    def __str__(self):
        if not self.items:
            return "[]"
        return "[" + " -> ".join(map(str, self.items)) + "]"
    def __next__(self):
        return self.next()
    def __iter__(self):
        return self
#9
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)
#10
class Summator:
    def transform(self, n):
        return n
    def sum(self, N):
        total = 0
        for n in range(1, N + 1):
            total += self.transform(n)
        return total
class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2
class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3
#11
class Summator:
    def transform(self, n):
        return n
    def sum(self, N):
        total = 0
        for n in range(1, N + 1):
            total += self.transform(n)
        return total
class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b
    def transform(self, n):
        return n ** self.b
class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(2)
class CubeSummator(PowerSummator):
    def __init__(self):
        super().__init__(3)
#12
class A:
    def __str__(self):
        return 'A.__str__ method'
    def hello(self):
        print('Hello')
class B:
    def __str__(self):
        return 'B.__str__ method'
    def good_evening(self):
        print('Good evening')
class C(A, B):
    pass
class D(B, A):
    pass
#13
class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range
    def hit(self, actor, target):
        if not target.is_alive():
            print("Враг уже повержен")
            return
        # Вычисляем расстояние между персонажами по формуле Пифагора
        ax, ay = actor.get_coords()
        tx, ty = target.get_coords()
        distance = math.sqrt((ax - tx)**2 + (ay - ty)**2)
        if distance > self.range:
            print(f"Враг слишком далеко для оружия {self.name}")
        else:
            print(f"Врагу нанесен урон оружием {self.name} в размере {self.damage}")
            target.get_damage(self.damage)
    def __str__(self):
        return self.name
    
class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp
    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y
    def is_alive(self):
        return self.hp > 0
    def get_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
    def get_coords(self):
        return (self.pos_x, self.pos_y)
    
class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon
    def hit(self, target):
        # Враг может бить только MainHero
        if not isinstance(target, MainHero):
            print("Могу ударить только Главного героя")
        else:
            self.weapon.hit(self, target)
    def __str__(self):
        return f"Враг на позиции ({self.pos_x}, {self.pos_y}) с оружием {self.weapon}"

class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.inventory = []
        self.current_weapon_idx = -1
    def hit(self, target):
        if self.current_weapon_idx == -1:
            print("Я безоружен")
            return
        # Герой может бить только BaseEnemy
        if not isinstance(target, BaseEnemy):
            print("Могу ударить только Врага")
        else:
            weapon = self.inventory[self.current_weapon_idx]
            weapon.hit(self, target)
    def add_weapon(self, weapon):
        if not isinstance(weapon, Weapon):
            print("Это не оружие")
            return
        print(f"Подобрал {weapon}")
        self.inventory.append(weapon)
        if len(self.inventory) == 1:
            self.current_weapon_idx = 0
    def next_weapon(self):
        if not self.inventory:
            print("Я безоружен")
        elif len(self.inventory) == 1:
            print("У меня только одно оружие")
        else:
            self.current_weapon_idx = (self.current_weapon_idx + 1) % len(self.inventory)
            weapon = self.inventory[self.current_weapon_idx]
            print(f"Сменил оружие на {weapon}")
    def heal(self, amount):
        self.hp += amount
        if self.hp > 200:
            self.hp = 200
        print(f"Полечился, теперь здоровья {self.hp}")
#14
class MailServer:
    def __init__(self, name):
        self.name = name
        # Хранилище писем: {имя_пользователя: [список писем]}
        self.mailboxes = {}
    def __str__(self):
        return f"Server({self.name})"
    def add_mail(self, user, message):
        if user not in self.mailboxes:
            self.mailboxes[user] = []
        self.mailboxes[user].append(message)
    def get_and_clear_mail(self, user):
        if user in self.mailboxes:
            messages = self.mailboxes[user][:]
            self.mailboxes[user] = []
            return messages
        return []

class MailNetwork:
    def __init__(self):
        self.allowed_servers = set()
    def register_server(self, server):
        self.allowed_servers.add(server)
    def is_allowed(self, server):
        return server in self.allowed_servers

class MailClient:
    def __init__(self, server, user, network):
        self.server = server
        self.user = user
        self.network = network  # Ссылка на сеть разрешенных серверов
    def receive_mail(self):
        messages = self.server.get_and_clear_mail(self.user)
        if not messages:
            return f"[{self.user}@{self.server.name}]: Новых писем нет."
        return f"[{self.user}@{self.server.name}] Получено писем ({len(messages)}): {messages}"
    def send_mail(self, target_server, target_user, message):
        # Проверка, есть ли целевой сервер в списке разрешенных
        if self.network.is_allowed(target_server):
            full_message = f"От {self.user} ({self.server.name}): {message}"
            target_server.add_mail(target_user, full_message)
            print(f"Успех: Письмо для {target_user} отправлено на {target_server.name}.")
        else:
            print(f"Ошибка: Сервер '{target_server.name}' не входит в список разрешенных. Отправка невозможна.")
#15
COMMANDS = {
    "make_negative": (lambda x: x > 0, lambda x: x * -1),
    "square": (lambda x: True, lambda x: x ** 2),
    "strange_command": (lambda x: x % 5 == 0, lambda x: x + 1),
}

def apply_transformations():
    try:
        line = input().split()
        if not line: return
        numbers = list(map(int, line))
        #Считываем количество команд
        n = int(input())
        for _ in range(n):
            cmd_name = input().strip()
            if cmd_name in COMMANDS:
                condition, transform = COMMANDS[cmd_name]
                # Создаем новый список, применяя трансформацию только к нужным числам
                numbers = [transform(x) if condition(x) else x for x in numbers]
            else:
                pass
        print(*(numbers))
    except (ValueError, EOFError):
        pass
#16
class MathFunction:
    def __call__(self, x):
        raise NotImplementedError

class Identity(MathFunction):
    def __call__(self, x):
        return x

class SqrtFun(MathFunction):
    def __call__(self, x):
        return math.sqrt(x)

class Constant(MathFunction):
    def __init__(self, value):
        self.value = value
    def __call__(self, x):
        return self.value

class Composite(MathFunction):
    def __init__(self, left, op_char, right):
        self.left = left
        self.right = right
        self.op_char = op_char
        # Словарь доступных операций
        self.operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }
        self.func = self.operations[op_char]
    def __call__(self, x):
        # Вычисляем левую и правую части, затем применяем оператор
        return self.func(self.left(x), self.right(x))
    
def solve():
    registry = {"x": Identity(), "sqrt_fun": SqrtFun()}
    def get_func(t):
        if t in registry: return registry[t]
        try: return Constant(float(t))
        except: return None
    # Читаем количество команд
    try:
        line = input().strip()
        if not line: return
        n = int(line)
    except (EOFError, ValueError):
        return
    for _ in range(n):
        try:
            line = input().strip()
            if not line: break
        except EOFError:
            break
        parts = line.split()
        if not parts: continue
        cmd = parts[0]
        if cmd == "define":
            registry[parts[1]] = Composite(get_func(parts[2]), parts[3], get_func(parts[4]))
        elif cmd == "calculate":
            f = registry.get(parts[1])
            if f:
                res = [f(float(x)) for x in parts[2:]]
                print(*(int(r) if r == int(r) else r for r in res))
#17
class Report:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = start_time# Время в минутах от начала дня
        self.duration = duration# Длительность в минутах
    @property
    def end_time(self):
        return self.start_time + self.duration
    def __str__(self):
        # Превращаем минуты обратно в формат HH:MM для вывода
        start_h, start_m = divmod(self.start_time, 60)
        end_h, end_m = divmod(self.end_time, 60)
        return f"[{start_h:02d}:{start_m:02d} - {end_h:02d}:{end_m:02d}] Тема: {self.topic} ({self.duration} мин.)"

class Conference:
    def __init__(self, name):
        self.name = name
        self.reports = []
    def add_report(self, topic, start_str, duration):
        # Преобразуем HH:MM в минуты для удобства расчетов
        try:
            h, m = map(int, start_str.split(':'))
            start_minutes = h * 60 + m
        except ValueError:
            print("Ошибка: Неверный формат времени! Используйте ЧЧ:ММ")
            return
        new_report = Report(topic, start_minutes, duration)
        # Проверка на перекрытия
        overlap = False
        for r in self.reports:
            # Условие перекрытия: (Начало1 < Конец2) И (Начало2 < Конец1)
            if new_report.start_time < r.end_time and r.start_time < new_report.end_time:
                overlap = True
                print(f"ПРЕДУПРЕЖДЕНИЕ: Доклад '{topic}' пересекается с докладом '{r.topic}'!")
        self.reports.append(new_report)
        # Сортируем доклады по времени начала после добавления
        self.reports.sort(key=lambda x: x.start_time)
        print(f"Доклад '{topic}' успешно добавлен.")
    def get_total_report_time(self):
        return sum(r.duration for r in self.reports)
    def get_longest_break(self):
        if len(self.reports) < 2:
            return 0
        max_break = 0
        for i in range(len(self.reports) - 1):
            current_break = self.reports[i+1].start_time - self.reports[i].end_time
            if current_break > max_break:
                max_break = current_break
        return max_break
    def show_schedule(self):
        print(f"\nРасписание конференции '{self.name}'")
        if not self.reports:
            print("Пока нет ни одного доклада.")
        for r in self.reports:
            print(r)
        print(f"\nСтатистика:")
        print(f"- Суммарное время докладов: {self.get_total_report_time()} мин.")
        print(f"- Самый долгий перерыв: {self.get_longest_break()} мин.")


def Conf_main():
    print("Добро пожаловать в планировщик конференций!")
    conf_name = input("Введите название конференции: ")
    my_conf = Conference(conf_name)
    while True:
        print("\nМЕНЮ:")
        print("1. Добавить новый доклад")
        print("2. Посмотреть расписание и статистику")
        print("3. Выход")
        choice = input("Выберите действие (1-3): ")
        if choice == '1':
            topic = input("Введите тему доклада: ")
            time_str = input("Введите время начала (ЧЧ:ММ): ")
            try:
                duration = int(input("Введите длительность в минутах: "))
                my_conf.add_report(topic, time_str, duration)
            except ValueError:
                print("Ошибка: Длительность должна быть числом!")
        elif choice == '2':
            my_conf.show_schedule()
        elif choice == '3':
            print("Программа завершена. Хорошей конференции!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")
#18
class File:
    def __init__(self, name, content=""):
        self.name = name
        self.content = content
class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirs = {}  # {имя: объект Directory}
        self.files = {}    # {имя: объект File}
    def list_content(self):
        # К папкам добавим '/', чтобы отличать их от файлов при выводе
        dirs = [name + "/" for name in self.subdirs.keys()]
        files = list(self.files.keys())
        return dirs + files
class FileSystem:
    def __init__(self):
        self.root = Directory("/")
    def _navigate(self, path, create_missing=False):
        parts = [p for p in path.split("/") if p]
        curr = self.root
        for part in parts:
            if part not in curr.subdirs:
                if create_missing:
                    curr.subdirs[part] = Directory(part)
                else:
                    return None
            curr = curr.subdirs[part]
        return curr
    def mkdir(self, path):
        self._navigate(path, create_missing=True)
        print(f"Директория '{path}' создана.")
    def ls(self, path):
        target = self._navigate(path)
        if target:
            content = target.list_content()
            print(f"Содержимое '{path}': {', '.join(content) if content else 'пусто'}")
        else:
            print(f"Ошибка: Директория '{path}' не найдена.")
    def write_file(self, path, content):
        parts = path.split("/")
        filename = parts[-1]
        dir_path = "/".join(parts[:-1])
        target_dir = self._navigate(dir_path, create_missing=True)
        # Если файл уже есть — перезаписываем контент, если нет — создаем новый
        if filename in target_dir.files:
            target_dir.files[filename].content = content
        else:
            target_dir.files[filename] = File(filename, content)
        print(f"Файл '{path}' записан.")
    def read_file(self, path):
        parts = path.split("/")
        filename = parts[-1]
        dir_path = "/".join(parts[:-1])
        target_dir = self._navigate(dir_path)
        if target_dir and filename in target_dir.files:
            print(f"Содержимое '{path}':\n{target_dir.files[filename].content}")
        else:
            print(f"Ошибка: Файл '{path}' не найден.")
def main():
    #1
    print("Задание 1:")
    bell = BigBell()
    bell.sound()
    bell.sound()
    bell.sound()
    balance = Balance()
    print("--------------------------")
    #2
    print("Задание 2:")
    balance.add_right(10)
    balance.add_left(9)
    balance.add_left(2)
    print(balance.result())
    balance2 = Balance()
    balance2.add_right(10)
    balance2.add_left(5)
    balance2.add_left(5)
    print(balance2.result())
    balance2.add_left(1)
    print(balance2.result())
    print("--------------------------")
    #3
    print("Задание 3:")
    values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
    selector = Selector(values)
    odds = selector.get_odds()
    evens = selector.get_evens()
    print(' '.join(map(str, odds)))
    print(' '.join(map(str, evens)))
    print("--------------------------")
    #4
    print("Задание 4:")
    p1 = Point(1, 2)
    p2 = Point(5, 6)
    if p1 == p2:
        print("Equal True")
    else:
        print("Equal False")
    if p1 != p2:
        print("Not equal True")
    else:
        print("Not equal False")
    print("--------------------------")
    #5
    print("Задание 5:")
    rl = ReversedList([10, 20, 30])
    for i in range(len(rl)):
        print(rl[i])
    print("Пример 2")
    rl2 = ReversedList([])
    print(len(rl2))
    print("--------------------------")
    #6
    print("Задание 6:")
    arr = SparseArray()
    arr[1] = 10
    arr[8] = 20
    for i in range(10):
        print('arr[{}] = {}'.format(i, arr[i]))
    index = 1000000000
    arr[index] = 123
    print('arr[{}] = {}'.format(index, arr[index]))
    print('arr[{}] = {}'.format(index - 1, arr[index - 1]))
    print("--------------------------")
    #7
    print("Задание 7:")
    poly = Polynomial([10, -1])
    print(poly(0))
    print(poly(1))
    print(poly(2))
    print("--------------------------")
    #8
    print("Задание 8:")
    q1 = Queue(1, 2, 3)
    print(q1)
    q1.append(4, 5)
    print(q1)
    qx = q1.copy()
    print(qx.pop())
    print(qx)
    q2 = q1.copy()
    print(q2)
    print(q1 == q2, id(q1) == id(q2))
    q3 = q2.next()
    print(q1, q2, q3, sep="\n")
    print(q1 + q3)
    q3.extend(Queue(1, 2))
    print(q3)
    q4 = Queue(1, 2)
    q4 += q3 >> 4
    print(q4)
    q5 = next(q4)
    print(q4)
    print(q5)
    print("--------------------------")
    #9
    print("Задание 9:")
    tri = Triangle(3, 4, 5)
    print(f"Периметр обычного треугольника: {tri.perimeter()}")
    eq_tri = EquilateralTriangle(10)
    print(f"Периметр равностороннего треугольника: {eq_tri.perimeter()}")
    print("--------------------------")
    #10
    print("Задание 10:")
    N = 10
    s = Summator()
    print(f"Сумма чисел до {N}: {s.sum(N)}")
    sq = SquareSummator()
    print(f"Сумма квадратов до {N}: {sq.sum(N)}")
    cb = CubeSummator()
    print(f"Сумма кубов до {N}: {cb.sum(N)}")
    print("--------------------------")
    #11
    print("Задание 11:")
    ps = PowerSummator(0.5)
    print(f"Сумма корней до 3: {ps.sum(3)}") 
    sq = SquareSummator()
    print(f"Сумма квадратов до 5: {sq.sum(5)}")
    cb = CubeSummator()
    print(f"Сумма кубов до 3: {cb.sum(3)}")
    print("--------------------------")
    #12
    print("Задание 12:")
    c = C()
    c.hello()
    c.good_evening()
    d = D()
    d.hello()
    d.good_evening()
    print(c)
    print(d)
    print("--------------------------")
    #13
    print("Задание 13:")
    weapon1 = Weapon("Короткий меч", 5, 1)
    weapon2 = Weapon("Длинный меч", 7, 2)
    weapon3 = Weapon("Лук", 3, 10)
    weapon4 = Weapon("Лазерная орбитальная пушка", 1000, 1000)
    princess = BaseCharacter(100, 100, 100)
    archer = BaseEnemy(50, 50, weapon3, 100)
    armored_swordsman = BaseEnemy(10, 10, weapon2, 500)
    archer.hit(armored_swordsman) # Могу ударить только Главного героя
    armored_swordsman.move(10, 10)
    print(armored_swordsman.get_coords())
    main_hero = MainHero(0, 0, "Король Артур", 200)
    main_hero.hit(armored_swordsman)
    main_hero.next_weapon()
    main_hero.add_weapon(weapon1)
    main_hero.hit(armored_swordsman)
    main_hero.add_weapon(weapon4)
    main_hero.hit(armored_swordsman)
    main_hero.next_weapon()
    main_hero.hit(princess)
    main_hero.hit(armored_swordsman)
    main_hero.hit(armored_swordsman)
    print("--------------------------")
    #14
    print("Задание 14:")
     # 1. Создаем "сеть", где будут регистрироваться серверы
    network = MailNetwork()
    # 2. Создаем серверы
    gmail = MailServer("gmail.com")
    yandex = MailServer("yandex.ru")
    secret_server = MailServer("private.onion")
    # 3. Регистрируем разрешенные серверы
    network.register_server(gmail)
    network.register_server(yandex)
    print("--- Список разрешенных серверов настроен (gmail, yandex) ---\n")
    # 4. Создаем клиентов
    alice = MailClient(gmail, "Alice", network)
    bob = MailClient(yandex, "Bob", network)
    # 5. Демонстрация отправки почты
    print("1. Элис отправляет письмо Бобу:")
    alice.send_mail(yandex, "Bob", "Привет, Боб! Как дела?")
    print("\n2. Боб проверяет почту:")
    print(bob.receive_mail())
    print("\n3. Боб проверяет почту второй раз (должно быть пусто):")
    print(bob.receive_mail())
    print("\n4. Попытка отправить письмо на незарегистрированный сервер:")
    # Пытаемся отправить письмо на secret_server, который не был добавлен в network
    alice.send_mail(secret_server, "Stranger", "Секретное сообщение")
    print("\n5. Элис отправляет письмо самой себе:")
    alice.send_mail(gmail, "Alice", "Не забыть купить хлеб.")
    print(alice.receive_mail())
    print("--------------------------")
    #15
    print("Задание 15:")
    apply_transformations()
    print("--------------------------")
    #16
    print("Задание 16:")
    solve()
    print("--------------------------")
    #17
    print("Задание 17:")
    Conf_main()
    print("--------------------------")
    #18
    fs = FileSystem()
    # 1. Создаем директории
    fs.mkdir("aaa/bbb")
    fs.mkdir("aaa/ccc")
    fs.mkdir("aaa/bbb/ccc")
    # 2. Пишем в файлы
    fs.write_file("1.txt", "Это корень")
    fs.write_file("aaa/1.txt", "Это файл в папке aaa")
    fs.write_file("aaa/bbb/1.txt", "Это файл глубоко внутри")
    # 3. Просмотр содержимого
    fs.ls("/")
    fs.ls("aaa")
    fs.ls("aaa/bbb")
    # 4. Чтение файлов
    fs.read_file("aaa/1.txt")
    fs.read_file("aaa/bbb/1.txt")
    # 5. Перезапись
    fs.write_file("aaa/1.txt", "Новое содержимое для aaa/1.txt")
    fs.read_file("aaa/1.txt")
if __name__ == "__main__":
    main()