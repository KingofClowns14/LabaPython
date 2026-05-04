import asyncio
import aiohttp
import time

#1
async def calculate_factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"[Factorial] Task {name}: Compute factorial({i})...")
        await asyncio.sleep(0.1) 
        f *= i
    print(f"[Factorial] Task {name}: Result = {f}")

async def run_factorial_app():
    print(">>> ЗАПУСК: Задание с факториалами")
    await asyncio.gather(
        calculate_factorial("A", 10),
        calculate_factorial("B", 5),
        calculate_factorial("C", 3),
    )
    print("<<< ЗАВЕРШЕНО: Задание с факториалами")

#2
SERVICES = {
    "ipify": "https://api.ipify.org",
    "ident.me": "https://ident.me",
    "icanhazip": "https://icanhazip.com"
}

async def fetch_ip(session, name, url):
    try:
        async with session.get(url, timeout=5) as response:
            if response.status == 200:
                ip = await response.text()
                return name, ip.strip()
    except:
        return None

async def run_ip_finder_app():
    print(">>> ЗАПУСК: Поиск IP")
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_ip(session, name, url) for name, url in SERVICES.items()]
        for completed in asyncio.as_completed(tasks):
            result = await completed
            if result:
                name, ip = result
                print(f"[IP Finder] Ответ получен от {name}: {ip}")
                break # Нам нужен только первый успешный
    print("<<< ЗАВЕРШЕНО: Поиск IP")
#3
async def person_interview(name, p1, d1, p2, d2):
    scale = 0.01 # Ускорение в 100 раз
    # 1 этап
    print(f"{name} started the 1 task.")
    await asyncio.sleep(p1 * scale)
    print(f"{name} moved on to the defense of the 1 task.")
    await asyncio.sleep(d1 * scale)
    print(f"{name} completed the 1 task.")
    # Отдых
    print(f"{name} is resting.")
    await asyncio.sleep(5 * scale)
    # 2 этап
    print(f"{name} started the 2 task.")
    await asyncio.sleep(p2 * scale)
    print(f"{name} moved on to the defense of the 2 task.")
    await asyncio.sleep(d2 * scale)
    print(f"{name} completed the 2 task.")

async def interviews(*args):
    tasks = [person_interview(*candidate) for candidate in args]
    await asyncio.gather(*tasks)

async def run_interviews_task():
    data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
    t0 = time.time()
    await interviews(*data)
    print(time.time() - t0)
#4
async def fertilizers(plant):
    # Подкормка (независимый процесс)
    print(f"7 Application of fertilizers for {plant}")
    await asyncio.sleep(3 / 1000)
    print(f"7 Fertilizers for the {plant} have been introduced")

async def pests_treatment(plant):
    # Обработка от вредителей (независимый процесс)
    print(f"8 Treatment of {plant} from pests")
    await asyncio.sleep(5 / 1000)
    print(f"8 The {plant} is treated from pests")

async def plant_lifecycle(name, soak_time, germ_time, root_time):
    # Основной жизненный цикл одного растения
    print(f"0 Beginning of sowing the {name} plant")
    print(f"1 Soaking of the {name} started")
    # Запускаем подкормку и защиту как фоновые задачи, они идут параллельно циклу
    asyncio.create_task(fertilizers(name))
    asyncio.create_task(pests_treatment(name))
    # Последовательные этапы
    await asyncio.sleep(soak_time / 1000)
    print(f"2 Soaking of the {name} is finished")
    print(f"3 Shelter of the {name} is supplied")
    await asyncio.sleep(germ_time / 1000)
    print(f"4 Shelter of the {name} is removed")
    print(f"5 The {name} has been transplanted")
    await asyncio.sleep(root_time / 1000)
    print(f"6 The {name} has taken root")
    print(f"9 The seedlings of the {name} are ready")

async def sowing(*args):
    # Запуск процесса для всех растений сразу
    tasks = [plant_lifecycle(*plant) for plant in args]
    await asyncio.gather(*tasks)


async def run_sowing_task():
    print(">>> ЗАПУСК: Посадка семян (Агроном)")
    data = [('carrot', 7, 18, 2), ('cabbage', 2, 6, 10), ('onion', 5, 12, 7)]
    await sowing(*data)
    print("<<< ЗАВЕРШЕНО: Посадка семян")

async def main():
    print("СТАРТ ВСЕЙ ПРОГРАММЫ\n")
    #1
    await run_factorial_app()
    print("----------------------")
    #2
    await run_ip_finder_app()
    print("----------------------")
    #3
    await run_interviews_task()
    print("----------------------")
    #4
    await run_sowing_task()
    print("\nВСЕ ЗАДАЧИ ВЫПОЛНЕНЫ")
    print("----------------------")
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass