import math
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
def main():
    # #1
    # print("Задание 1:")
    # bell = BigBell()
    # bell.sound()
    # bell.sound()
    # bell.sound()
    # balance = Balance()
    # print("--------------------------")
    # #2
    # print("Задание 2:")
    # balance.add_right(10)
    # balance.add_left(9)
    # balance.add_left(2)
    # print(balance.result())
    # balance2 = Balance()
    # balance2.add_right(10)
    # balance2.add_left(5)
    # balance2.add_left(5)
    # print(balance2.result())
    # balance2.add_left(1)
    # print(balance2.result())
    # print("--------------------------")
    # #3
    # print("Задание 3:")
    # values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
    # selector = Selector(values)
    # odds = selector.get_odds()
    # evens = selector.get_evens()
    # print(' '.join(map(str, odds)))
    # print(' '.join(map(str, evens)))
    # print("--------------------------")
    # #4
    # print("Задание 4:")
    # p1 = Point(1, 2)
    # p2 = Point(5, 6)
    # if p1 == p2:
    #     print("Equal True")
    # else:
    #     print("Equal False")
    # if p1 != p2:
    #     print("Not equal True")
    # else:
    #     print("Not equal False")
    # print("--------------------------")
    # #5
    # print("Задание 5:")
    # rl = ReversedList([10, 20, 30])
    # for i in range(len(rl)):
    #     print(rl[i])
    # print("Пример 2")
    # rl2 = ReversedList([])
    # print(len(rl2))
    # print("--------------------------")
    # #6
    # print("Задание 6:")
    # arr = SparseArray()
    # arr[1] = 10
    # arr[8] = 20
    # for i in range(10):
    #     print('arr[{}] = {}'.format(i, arr[i]))
    # index = 1000000000
    # arr[index] = 123
    # print('arr[{}] = {}'.format(index, arr[index]))
    # print('arr[{}] = {}'.format(index - 1, arr[index - 1]))
    # print("--------------------------")
    # #7
    # print("Задание 7:")
    # poly = Polynomial([10, -1])
    # print(poly(0))
    # print(poly(1))
    # print(poly(2))
    # print("--------------------------")
    # #8
    # print("Задание 8:")
    # q1 = Queue(1, 2, 3)
    # print(q1)
    # q1.append(4, 5)
    # print(q1)
    # qx = q1.copy()
    # print(qx.pop())
    # print(qx)
    # q2 = q1.copy()
    # print(q2)
    # print(q1 == q2, id(q1) == id(q2))
    # q3 = q2.next()
    # print(q1, q2, q3, sep="\n")
    # print(q1 + q3)
    # q3.extend(Queue(1, 2))
    # print(q3)
    # q4 = Queue(1, 2)
    # q4 += q3 >> 4
    # print(q4)
    # q5 = next(q4)
    # print(q4)
    # print(q5)
    # print("--------------------------")
    # #9
    # print("Задание 9:")
    # tri = Triangle(3, 4, 5)
    # print(f"Периметр обычного треугольника: {tri.perimeter()}")
    # eq_tri = EquilateralTriangle(10)
    # print(f"Периметр равностороннего треугольника: {eq_tri.perimeter()}")
    # print("--------------------------")
    # #10
    # print("Задание 10:")
    # N = 10
    # s = Summator()
    # print(f"Сумма чисел до {N}: {s.sum(N)}")
    # sq = SquareSummator()
    # print(f"Сумма квадратов до {N}: {sq.sum(N)}")
    # cb = CubeSummator()
    # print(f"Сумма кубов до {N}: {cb.sum(N)}")
    # print("--------------------------")
    # #11
    # print("Задание 11:")
    # ps = PowerSummator(0.5)
    # print(f"Сумма корней до 3: {ps.sum(3)}") 
    # sq = SquareSummator()
    # print(f"Сумма квадратов до 5: {sq.sum(5)}")
    # cb = CubeSummator()
    # print(f"Сумма кубов до 3: {cb.sum(3)}")
    # print("--------------------------")
    # #12
    # print("Задание 12:")
    # c = C()
    # c.hello()
    # c.good_evening()
    # d = D()
    # d.hello()
    # d.good_evening()
    # print(c)
    # print(d)
    # print("--------------------------")
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
if __name__ == "__main__":
    main()